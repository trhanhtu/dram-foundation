// =============================================================================
// DRAM Foundation VN - Open Hardware Firmware
// Device: Gen 1 Photoresist Spin Coater Closed-Loop RPM Controller
// Target MCU: ESP32 DevKit V1 (240MHz)
// Motor: A2212 1000KV BLDC Motor + 30A ESC (50Hz Servo PWM 1000us - 2000us)
// Sensor: Optical Slot Tachometer (20 slots per revolution)
// Actuator: 12V Mini Vacuum Pump Relay
// Safety: Physical Lid Microswitch Interlock
// =============================================================================

#include <Arduino.h>

// Pin Definitions
const int PIN_ESC_PWM     = 13; // PWM Output to ESC signal line
const int PIN_TACH_INT    = 14; // Optical tachometer pulse input (Interrupt)
const int PIN_VAC_PUMP    = 27; // Relay control for 12V vacuum pump (Active HIGH)
const int PIN_LID_SWITCH  = 26; // Safety lid switch (Internal PULLUP, LOW = CLOSED)
const int PIN_BTN_START   = 25; // Pushbutton to start cycle (PULLUP)
const int PIN_STATUS_LED  = 2;  // Onboard blue LED

// Tachometer & Timing Constants
const int ENCODER_SLOTS   = 20;   // 20 pulses per full revolution
const unsigned long TACH_WINDOW_MS = 100; // Sample every 100ms

// PID Control Coefficients for BLDC Velocity Loop
float Kp = 0.15;
float Ki = 0.05;
float Kd = 0.02;

// State Variables
volatile unsigned long tach_pulse_count = 0;
unsigned long last_tach_calc_ms = 0;
float current_rpm = 0.0;
float target_rpm  = 0.0;
float pid_integral = 0.0;
float last_error   = 0.0;

int current_pwm_us = 1000; // 1000us = Stop, 2000us = Full throttle
bool is_spinning   = false;

// Interrupt Service Routine for Tachometer
void IRAM_ATTR onTachPulse() {
  tach_pulse_count++;
}

// Low-level software PWM pulse generator for standard 50Hz RC ESC
void setThrottleUs(int pulse_us) {
  pulse_us = constrain(pulse_us, 1000, 2000);
  current_pwm_us = pulse_us;
  
  digitalWrite(PIN_ESC_PWM, HIGH);
  delayMicroseconds(pulse_us);
  digitalWrite(PIN_ESC_PWM, LOW);
}

void setup() {
  Serial.begin(115200);
  delay(500);

  pinMode(PIN_ESC_PWM, OUTPUT);
  pinMode(PIN_VAC_PUMP, OUTPUT);
  pinMode(PIN_STATUS_LED, OUTPUT);
  pinMode(PIN_LID_SWITCH, INPUT_PULLUP);
  pinMode(PIN_BTN_START, INPUT_PULLUP);
  pinMode(PIN_TACH_INT, INPUT_PULLUP);

  digitalWrite(PIN_VAC_PUMP, LOW);
  digitalWrite(PIN_STATUS_LED, LOW);
  setThrottleUs(1000); // Initialize ESC at zero throttle (Arming tone)

  attachInterrupt(digitalPinToInterrupt(PIN_TACH_INT), onTachPulse, RISING);

  Serial.println(F("\n========================================================"));
  Serial.println(F(" DRAM Foundation VN - Gen 1 Spin Coater Controller"));
  Serial.println(F(" 2-Stage Recipe: 500 RPM (5s) -> 4,000 RPM (30s)"));
  Serial.println(F(" Safety: Lid Switch Interlock Enabled"));
  Serial.println(F(" Commands: START, STOP, VAC ON, VAC OFF, SET <rpm>"));
  Serial.println(F("========================================================"));

  // Send 1000us arming pulses for 2 seconds
  for (int i = 0; i < 100; i++) {
    setThrottleUs(1000);
    delay(20);
  }
  Serial.println(F("[ESC] Arming sequence complete. Ready for spin cycle."));
}

// Compute live RPM from tachometer interrupts
void updateRpmCalculation() {
  unsigned long now = millis();
  if (now - last_tach_calc_ms >= TACH_WINDOW_MS) {
    noInterrupts();
    unsigned long pulses = tach_pulse_count;
    tach_pulse_count = 0;
    interrupts();

    float dt_sec = (now - last_tach_calc_ms) / 1000.0;
    current_rpm = (pulses / (float)ENCODER_SLOTS) * (60.0 / dt_sec);
    last_tach_calc_ms = now;
  }
}

// Closed-loop PID controller update
void updateVelocityPID() {
  if (target_rpm <= 0.0) {
    setThrottleUs(1000);
    pid_integral = 0.0;
    return;
  }

  float error = target_rpm - current_rpm;
  pid_integral += error * 0.02;
  pid_integral = constrain(pid_integral, -200.0, 200.0);
  float derivative = (error - last_error) / 0.02;
  last_error = error;

  // Base feed-forward estimate (approx 0.16 us/RPM for 1000KV motor on 12V)
  float feed_forward = 1000.0 + (target_rpm * 0.16);
  float output = feed_forward + (Kp * error) + (Ki * pid_integral) + (Kd * derivative);
  
  setThrottleUs((int)output);
}

// Execute 2-stage standard semiconductor coating recipe
void runSpinCoatingRecipe(int stage1_rpm = 500, int stage1_sec = 5, int stage2_rpm = 4000, int stage2_sec = 30) {
  // 1. Safety check
  if (digitalRead(PIN_LID_SWITCH) == HIGH) {
    Serial.println(F("[ERROR] Cannot start: Safety lid is OPEN!"));
    return;
  }

  is_spinning = true;
  digitalWrite(PIN_STATUS_LED, HIGH);

  // 2. Engage vacuum hold-down pump
  Serial.println(F("[STEP 1] Engaging Vacuum Chuck Pump (Holding wafer)..."));
  digitalWrite(PIN_VAC_PUMP, HIGH);
  delay(1500); // Wait for vacuum to build up (< -50 kPa)

  // 3. Stage 1: Resist Spreading
  Serial.println(F("[STEP 2] Stage 1: Spreading resist at 500 RPM for 5 seconds..."));
  target_rpm = stage1_rpm;
  unsigned long start_time = millis();
  while (millis() - start_time < (unsigned long)(stage1_sec * 1000)) {
    if (digitalRead(PIN_LID_SWITCH) == HIGH) { emergencyHalt(); return; }
    updateRpmCalculation();
    updateVelocityPID();
    delay(20);
  }

  // 4. Stage 2: High-Speed Planarization & Solvent Thinning
  Serial.println(F("[STEP 3] Stage 2: High-speed thinning at 4,000 RPM for 30 seconds..."));
  target_rpm = stage2_rpm;
  start_time = millis();
  while (millis() - start_time < (unsigned long)(stage2_sec * 1000)) {
    if (digitalRead(PIN_LID_SWITCH) == HIGH) { emergencyHalt(); return; }
    updateRpmCalculation();
    updateVelocityPID();
    
    // Log telemetry every 1 second
    if ((millis() - start_time) % 1000 < 25) {
      Serial.print(F("[RUN] Target: ")); Serial.print(target_rpm);
      Serial.print(F(" | Actual: ")); Serial.print(current_rpm);
      Serial.println(F(" RPM"));
    }
    delay(20);
  }

  // 5. Deceleration Ramp
  Serial.println(F("[STEP 4] Decelerating motor smoothly..."));
  target_rpm = 0.0;
  for (int p = current_pwm_us; p >= 1000; p -= 20) {
    setThrottleUs(p);
    delay(30);
  }
  setThrottleUs(1000);
  delay(2000); // Wait for chuck to completely stop

  // 6. Release vacuum chuck
  Serial.println(F("[STEP 5] Disengaging vacuum pump. Wafer ready for Softbake!"));
  digitalWrite(PIN_VAC_PUMP, LOW);
  digitalWrite(PIN_STATUS_LED, LOW);
  is_spinning = false;
  Serial.println(F("[RECIPE COMPLETE] Transfer wafer to 90 deg C hotplate within Q-Time limit!"));
}

// Emergency safety stop
void emergencyHalt() {
  target_rpm = 0.0;
  setThrottleUs(1000);
  digitalWrite(PIN_VAC_PUMP, LOW);
  digitalWrite(PIN_STATUS_LED, LOW);
  is_spinning = false;
  Serial.println(F("\n[EMERGENCY HALT] Safety lid opened during spin cycle! Motor cut immediately!"));
}

void loop() {
  updateRpmCalculation();

  // Continuous safety monitor
  if (is_spinning && digitalRead(PIN_LID_SWITCH) == HIGH) {
    emergencyHalt();
  }

  // Hardware pushbutton trigger
  if (digitalRead(PIN_BTN_START) == LOW && !is_spinning) {
    delay(50); // Debounce
    if (digitalRead(PIN_BTN_START) == LOW) {
      runSpinCoatingRecipe();
    }
  }

  // Serial commands
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim(); cmd.toUpperCase();
    if (cmd == "START") {
      runSpinCoatingRecipe();
    } else if (cmd == "STOP") {
      emergencyHalt();
    } else if (cmd == "VAC ON") {
      digitalWrite(PIN_VAC_PUMP, HIGH);
      Serial.println(F("[VAC] Pump ON"));
    } else if (cmd == "VAC OFF") {
      digitalWrite(PIN_VAC_PUMP, LOW);
      Serial.println(F("[VAC] Pump OFF"));
    } else if (cmd.startsWith("SET ")) {
      target_rpm = cmd.substring(4).toFloat();
      Serial.print(F("[SET] Manual Target RPM set to: ")); Serial.println(target_rpm);
    }
  }

  // Routine PWM refresh for ESC keep-alive (50Hz)
  if (!is_spinning) {
    setThrottleUs(1000);
    delay(20);
  }
}
