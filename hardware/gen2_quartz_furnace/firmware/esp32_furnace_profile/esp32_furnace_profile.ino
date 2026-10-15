// =============================================================================
// DRAM Foundation VN - Open Hardware Firmware
// Device: Gen 2 Quartz Tube Furnace Deal-Grove Profile Controller
// Target MCU: ESP32 DevKit V1 (240MHz)
// Temperature Sensor: Thermocouple Type K via MAX6675 / MAX31855 (SPI)
// Heating Actuator: Solid State Relay SSR-40DA (Time-Proportional Window)
// Gas Actuators: 12V Solenoid Valves for High-Purity N2 & O2
//
// Process Thermal Profile (Deal-Grove Dry Oxidation for 45nm Gate Oxide):
//   1. Pre-Purge       : N2 ON  | Room Temp   | 10 min
//   2. Ramp-Up         : N2 ON  | Ramp 10C/min| Up to 1,000C
//   3. Oxidation Soak  : O2 ON  | Hold 1,000C | 60 min
//   4. Post-Anneal     : N2 ON  | Hold 1,000C | 15 min
//   5. Controlled Cool : N2 ON  | Cool 5C/min | Down to 400C
// =============================================================================

#include <Arduino.h>

// Pin Definitions
const int PIN_SSR       = 23; // SSR Output (Active HIGH)
const int PIN_VALVE_N2  = 18; // Solenoid Valve N2 (Active HIGH)
const int PIN_VALVE_O2  = 19; // Solenoid Valve O2 (Active HIGH)
const int PIN_TC_CS     = 5;  // MAX6675 Chip Select
const int PIN_TC_SCK    = 14; // MAX6675 Clock
const int PIN_TC_SO     = 12; // MAX6675 MISO / Data Out
const int PIN_STATUS_LED= 2;  // Onboard status LED

// PID Temperature Control Constants
float Kp = 3.5;
float Ki = 0.08;
float Kd = 12.0;

// Heating Window: 1000 ms time-proportional cycle
const unsigned long WINDOW_SIZE_MS = 1000;
unsigned long window_start_time = 0;
float duty_cycle_pct = 0.0; // 0.0 to 100.0%

// Profile State Machine
enum FurnaceStage {
  STAGE_IDLE,
  STAGE_PURGE_N2,
  STAGE_RAMP_UP,
  STAGE_SOAK_OX,
  STAGE_ANNEAL_N2,
  STAGE_COOL_DOWN,
  STAGE_COMPLETE
};

FurnaceStage current_stage = STAGE_IDLE;
unsigned long stage_start_time = 0;
float current_setpoint_c = 25.0;
float measured_temp_c   = 25.0;
float pid_integral      = 0.0;
float last_error        = 0.0;

// Low-level SPI read for MAX6675 Thermocouple converter
float readMAX6675() {
  uint16_t raw_data = 0;
  digitalWrite(PIN_TC_CS, LOW);
  delayMicroseconds(2);

  for (int i = 15; i >= 0; i--) {
    digitalWrite(PIN_TC_SCK, HIGH);
    delayMicroseconds(2);
    if (digitalRead(PIN_TC_SO)) {
      raw_data |= (1 << i);
    }
    digitalWrite(PIN_TC_SCK, LOW);
    delayMicroseconds(2);
  }
  digitalWrite(PIN_TC_CS, HIGH);

  // Check thermocouple open circuit bit D2
  if (raw_data & 0x04) {
    Serial.println(F("[ALERT] Thermocouple disconnected or open circuit!"));
    return -999.0;
  }

  // D14..D3 contains temperature in 0.25 C increments
  raw_data >>= 3;
  return raw_data * 0.25;
}

void setGasEnvironment(bool n2_on, bool o2_on) {
  // Safety interlock: Never allow both N2 and O2 valves to open simultaneously
  if (n2_on && o2_on) {
    o2_on = false; // Prioritize inert gas
  }
  digitalWrite(PIN_VALVE_N2, n2_on ? HIGH : LOW);
  digitalWrite(PIN_VALVE_O2, o2_on ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  delay(500);

  pinMode(PIN_SSR, OUTPUT);
  pinMode(PIN_VALVE_N2, OUTPUT);
  pinMode(PIN_VALVE_O2, OUTPUT);
  pinMode(PIN_STATUS_LED, OUTPUT);
  pinMode(PIN_TC_CS, OUTPUT);
  pinMode(PIN_TC_SCK, OUTPUT);
  pinMode(PIN_TC_SO, INPUT);

  digitalWrite(PIN_SSR, LOW);
  setGasEnvironment(false, false);
  digitalWrite(PIN_TC_CS, HIGH);
  digitalWrite(PIN_TC_SCK, LOW);

  window_start_time = millis();

  Serial.println(F("\n========================================================"));
  Serial.println(F(" DRAM Foundation VN - Gen 2 Quartz Tube Furnace Profile"));
  Serial.println(F(" Controller: ESP32 + MAX6675 | SSR Time-Proportional PID"));
  Serial.println(F(" Deal-Grove Dry Ox Profile: 1000 C Soak for 60 min"));
  Serial.println(F(" Output Format: TIME_S,STAGE,SETPOINT_C,TEMP_C,DUTY_PCT,GAS"));
  Serial.println(F(" Commands: START, ABORT, STATUS"));
  Serial.println(F("========================================================"));
}

// Compute Time-Proportional PID
void computeThermalPID() {
  if (current_stage == STAGE_IDLE || current_stage == STAGE_COMPLETE) {
    duty_cycle_pct = 0.0;
    digitalWrite(PIN_SSR, LOW);
    return;
  }

  float error = current_setpoint_c - measured_temp_c;
  
  // Anti-windup clamping on integral
  if (abs(error) < 50.0) {
    pid_integral += error;
    pid_integral = constrain(pid_integral, -100.0, 100.0);
  }

  float derivative = error - last_error;
  last_error = error;

  float output = (Kp * error) + (Ki * pid_integral) + (Kd * derivative);
  duty_cycle_pct = constrain(output, 0.0, 100.0);
}

// Time-proportional SSR actuation within 1000ms window
void updateSSRWindow() {
  unsigned long now = millis();
  if (now - window_start_time >= WINDOW_SIZE_MS) {
    window_start_time = now;
  }

  unsigned long on_time_ms = (unsigned long)((duty_cycle_pct / 100.0) * WINDOW_SIZE_MS);
  if (now - window_start_time < on_time_ms && duty_cycle_pct > 0.0) {
    digitalWrite(PIN_SSR, HIGH);
    digitalWrite(PIN_STATUS_LED, HIGH);
  } else {
    digitalWrite(PIN_SSR, LOW);
    digitalWrite(PIN_STATUS_LED, LOW);
  }
}

// Thermal state machine executing Deal-Grove sequence
void updateFurnaceStateMachine() {
  unsigned long elapsed_stage_s = (millis() - stage_start_time) / 1000;

  switch (current_stage) {
    case STAGE_IDLE:
      current_setpoint_c = 25.0;
      setGasEnvironment(false, false);
      break;

    case STAGE_PURGE_N2:
      // Stage 1: Purge ambient air with N2 for 10 minutes (600s)
      setGasEnvironment(true, false);
      current_setpoint_c = 25.0;
      if (elapsed_stage_s >= 600) {
        current_stage = STAGE_RAMP_UP;
        stage_start_time = millis();
        Serial.println(F("[TRANSITION] Purge complete -> Ramping up to 1,000 C in N2..."));
      }
      break;

    case STAGE_RAMP_UP:
      // Stage 2: Ramp up to 1,000 C at 10 C/min (~0.167 C/s)
      setGasEnvironment(true, false);
      current_setpoint_c = min(1000.0f, 25.0f + (float)(elapsed_stage_s * (10.0 / 60.0)));
      if (measured_temp_c >= 995.0 && current_setpoint_c >= 1000.0) {
        current_stage = STAGE_SOAK_OX;
        stage_start_time = millis();
        Serial.println(F("[TRANSITION] Temperature reached 1,000 C -> Switching to DRY O2 for 60 min..."));
      }
      break;

    case STAGE_SOAK_OX:
      // Stage 3: Hold 1,000 C in pure O2 for 60 minutes (3,600s)
      setGasEnvironment(false, true);
      current_setpoint_c = 1000.0;
      if (elapsed_stage_s >= 3600) {
        current_stage = STAGE_ANNEAL_N2;
        stage_start_time = millis();
        Serial.println(F("[TRANSITION] Oxidation complete -> Post-anneal in N2 for 15 min..."));
      }
      break;

    case STAGE_ANNEAL_N2:
      // Stage 4: Hold 1,000 C in N2 for 15 minutes (900s)
      setGasEnvironment(true, false);
      current_setpoint_c = 1000.0;
      if (elapsed_stage_s >= 900) {
        current_stage = STAGE_COOL_DOWN;
        stage_start_time = millis();
        Serial.println(F("[TRANSITION] Anneal complete -> Controlled cooling in N2..."));
      }
      break;

    case STAGE_COOL_DOWN:
      // Stage 5: Ramp down to 400 C at 5 C/min
      setGasEnvironment(true, false);
      current_setpoint_c = max(400.0f, 1000.0f - (float)(elapsed_stage_s * (5.0 / 60.0)));
      if (measured_temp_c <= 405.0) {
        current_stage = STAGE_COMPLETE;
        setGasEnvironment(false, false);
        digitalWrite(PIN_SSR, LOW);
        Serial.println(F("[FURNACE COMPLETE] Wafer oxidation finished! Ready to unload boat."));
      }
      break;

    case STAGE_COMPLETE:
      current_setpoint_c = 25.0;
      break;
  }
}

void loop() {
  static unsigned long last_1s_log = 0;
  
  // 1. Actuate SSR fast loop
  updateSSRWindow();

  // 2. 1-Second Periodic Control & Telemetry
  if (millis() - last_1s_log >= 1000) {
    last_1s_log = millis();

    // Read Thermocouple
    float t = readMAX6675();
    if (t > -100.0) {
      measured_temp_c = t;
    }

    // Safety: Overtemperature cutoff
    if (measured_temp_c > 1150.0) {
      digitalWrite(PIN_SSR, LOW);
      current_stage = STAGE_IDLE;
      Serial.println(F("[EMERGENCY] Overtemperature > 1,150 C detected! Heater cut immediately!"));
    }

    // Update state machine and PID
    updateFurnaceStateMachine();
    computeThermalPID();

    // Telemetry CSV Output
    const char* stage_str = "IDLE";
    if (current_stage == STAGE_PURGE_N2) stage_str = "PURGE_N2";
    else if (current_stage == STAGE_RAMP_UP) stage_str = "RAMP_UP";
    else if (current_stage == STAGE_SOAK_OX) stage_str = "SOAK_O2";
    else if (current_stage == STAGE_ANNEAL_N2) stage_str = "ANNEAL_N2";
    else if (current_stage == STAGE_COOL_DOWN) stage_str = "COOLING";
    else if (current_stage == STAGE_COMPLETE) stage_str = "COMPLETE";

    const char* gas_str = (digitalRead(PIN_VALVE_O2) == HIGH) ? "O2" : ((digitalRead(PIN_VALVE_N2) == HIGH) ? "N2" : "OFF");

    Serial.print(millis() / 1000); Serial.print(F(","));
    Serial.print(stage_str); Serial.print(F(","));
    Serial.print(current_setpoint_c, 1); Serial.print(F(","));
    Serial.print(measured_temp_c, 1); Serial.print(F(","));
    Serial.print(duty_cycle_pct, 1); Serial.print(F(","));
    Serial.println(gas_str);
  }

  // Serial Commands
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim(); cmd.toUpperCase();
    if (cmd == "START" && current_stage == STAGE_IDLE) {
      current_stage = STAGE_PURGE_N2;
      stage_start_time = millis();
      Serial.println(F("[CMD] Deal-Grove Oxidation Sequence Initiated."));
    } else if (cmd == "ABORT") {
      current_stage = STAGE_IDLE;
      digitalWrite(PIN_SSR, LOW);
      setGasEnvironment(false, false);
      Serial.println(F("[CMD] Sequence Aborted. Heater & Gases shut off."));
    } else if (cmd == "STATUS") {
      Serial.print(F("Stage: ")); Serial.print(current_stage);
      Serial.print(F(" | Setpoint: ")); Serial.print(current_setpoint_c);
      Serial.print(F(" C | Temp: ")); Serial.print(measured_temp_c);
      Serial.println(F(" C"));
    }
  }
}
