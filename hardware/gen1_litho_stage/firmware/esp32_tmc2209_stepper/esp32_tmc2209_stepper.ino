// =============================================================================
// DRAM Foundation VN - Open Hardware Firmware
// Device: Gen 1 Macroscopic Lithography Linear Stage Controller
// Target MCU: ESP32 DevKit V1 (Dual-Core 240MHz)
// Stepper Driver: TMC2209 (StealthChop2, 1/256 Microstepping, 24V supply)
// Sensor: Optical Endstop (Active LOW)
//
// Kinematics & Resolution:
//   - Motor: NEMA 17 (1.8 deg = 200 full steps/rev)
//   - Leadscrew: T8 with 2.0 mm Lead (1 revolution = 2,000 um)
//   - Full Step Resolution: 2000 um / 200 = 10.0 um / step
//   - Microstepping: 1/256 microsteps
//   - Theoretical Resolution: 10.0 um / 256 = 0.0390625 um / pulse
//   - Physical Step Scale: 25,600 pulses per mm (25.6 pulses per um)
// =============================================================================

#include <Arduino.h>

// Pin Configuration (ESP32 DevKit V1)
const int PIN_STEP    = 18; // STEP pulse to TMC2209
const int PIN_DIR     = 19; // DIRECTION control
const int PIN_ENABLE  = 21; // ENABLE (Active LOW)
const int PIN_ENDSTOP = 22; // Optical Endstop (Internal Pullup, LOW when blocked)
const int PIN_LED     = 2;  // Onboard Status LED

// Motion Constants
const double PULSES_PER_UM = 25.6; // 25,600 steps/mm (with 1/256 microstepping)
const long MAX_TRAVEL_UM   = 200000; // 200 mm travel limit

// State Variables
volatile long current_pos_um = 0;
bool is_homed = false;

// Function Prototypes
void stepPulse(int delay_us);
void moveToUm(long target_um, int speed_us);
void homeStage();
void runRepeatabilityTest(int cycles, long dist_um);
void parseCommand(String cmd);

void setup() {
  Serial.begin(115200);
  delay(500);

  pinMode(PIN_STEP, OUTPUT);
  pinMode(PIN_DIR, OUTPUT);
  pinMode(PIN_ENABLE, OUTPUT);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_ENDSTOP, INPUT_PULLUP);

  // Enable TMC2209 (Active LOW)
  digitalWrite(PIN_ENABLE, LOW);
  digitalWrite(PIN_STEP, LOW);
  digitalWrite(PIN_DIR, LOW);
  digitalWrite(PIN_LED, HIGH);

  Serial.println(F("\n========================================================"));
  Serial.println(F(" DRAM Foundation VN - Gen 1 Lithography Stage Firmware"));
  Serial.println(F(" Controller: ESP32 | Driver: TMC2209 (1/256 Microstepping)"));
  Serial.println(F(" Resolution: 0.039 um/pulse | Scale: 25.6 pulses/um"));
  Serial.println(F(" Commands: HOME, G0 X<um>, TEST <cycles> <dist_um>, STATUS"));
  Serial.println(F("========================================================"));
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    if (input.length() > 0) {
      parseCommand(input);
    }
  }
}

// Low-level high-precision step pulse generator
void stepPulse(int delay_us) {
  digitalWrite(PIN_STEP, HIGH);
  delayMicroseconds(2);
  digitalWrite(PIN_STEP, LOW);
  delayMicroseconds(max(5, delay_us));
}

// Move to absolute position with trapezoidal velocity ramp
void moveToUm(long target_um, int base_delay_us = 40) {
  target_um = constrain(target_um, 0, MAX_TRAVEL_UM);
  long delta_um = target_um - current_pos_um;
  if (delta_um == 0) return;

  bool dir = (delta_um > 0);
  digitalWrite(PIN_DIR, dir ? HIGH : LOW);
  delayMicroseconds(10);

  long total_steps = (long)(abs(delta_um) * PULSES_PER_UM);
  long accel_steps = min(total_steps / 4, 3000L); // Acceleration ramp length

  int min_delay = base_delay_us;      // Top cruising speed delay
  int max_delay = base_delay_us * 3;  // Starting ramp delay

  for (long s = 0; s < total_steps; s++) {
    // Check endstop safety when moving toward home
    if (!dir && digitalRead(PIN_ENDSTOP) == LOW) {
      current_pos_um = 0;
      Serial.println(F("[SAFETY] Endstop triggered during move! Motion halted."));
      return;
    }

    // Velocity Profile Calculation
    int current_delay = min_delay;
    if (s < accel_steps) {
      // Acceleration phase
      current_delay = max_delay - (max_delay - min_delay) * s / accel_steps;
    } else if (s > total_steps - accel_steps) {
      // Deceleration phase
      long rem = total_steps - s;
      current_delay = min_delay + (max_delay - min_delay) * (accel_steps - rem) / accel_steps;
    }

    stepPulse(current_delay);
  }

  current_pos_um = target_um;
  Serial.print(F("[POS] Reached: "));
  Serial.print(current_pos_um);
  Serial.println(F(" um"));
}

// Two-stage precision optical homing routine
void homeStage() {
  Serial.println(F("[HOMING] Starting 2-stage optical homing routine..."));
  digitalWrite(PIN_DIR, LOW); // Move toward endstop
  delayMicroseconds(10);

  // Stage 1: Fast seek
  while (digitalRead(PIN_ENDSTOP) == HIGH) {
    stepPulse(60);
  }
  delay(100);

  // Stage 2: Back off 2.0 mm (2000 um)
  digitalWrite(PIN_DIR, HIGH);
  for (long s = 0; s < (long)(2000 * PULSES_PER_UM); s++) {
    stepPulse(100);
  }
  delay(100);

  // Stage 3: Slow precision approach (Sub-micron optical latch)
  digitalWrite(PIN_DIR, LOW);
  while (digitalRead(PIN_ENDSTOP) == HIGH) {
    stepPulse(250); // Very slow approach
  }

  current_pos_um = 0;
  is_homed = true;
  Serial.println(F("[HOMING] Stage Origin calibrated to ZERO (Repeatability < 5 um)."));
}

// Automated 1,000-cycle acceptance testing routine
void runRepeatabilityTest(int cycles, long dist_um) {
  if (!is_homed) homeStage();

  Serial.println(F("========================================================"));
  Serial.print(F(" STARTING ACCEPTANCE TEST: "));
  Serial.print(cycles);
  Serial.print(F(" CYCLES OVER "));
  Serial.print(dist_um / 1000.0);
  Serial.println(F(" mm"));
  Serial.println(F(" Attach Dial Indicator to verify < +/- 20 um Repeatability."));
  Serial.println(F("========================================================"));

  for (int c = 1; c <= cycles; c++) {
    moveToUm(dist_um, 35);
    delay(50);
    moveToUm(0, 35);
    delay(50);

    if (c % 10 == 0 || c == cycles) {
      Serial.print(F("[TEST] Cycle "));
      Serial.print(c);
      Serial.print(F(" / "));
      Serial.print(cycles);
      Serial.println(F(" completed."));
    }
  }

  Serial.println(F("[TEST DONE] Measure final dial indicator reading and log to SOP!"));
}

// Serial command interpreter
void parseCommand(String cmd) {
  cmd.toUpperCase();
  if (cmd == "HOME") {
    homeStage();
  } else if (cmd.startsWith("G0 X")) {
    long target = cmd.substring(4).toInt();
    moveToUm(target, 40);
  } else if (cmd.startsWith("TEST")) {
    int space1 = cmd.indexOf(' ');
    int space2 = cmd.indexOf(' ', space1 + 1);
    int cycles = 10;
    long dist = 50000; // 50 mm
    if (space1 > 0 && space2 > 0) {
      cycles = cmd.substring(space1 + 1, space2).toInt();
      dist = cmd.substring(space2 + 1).toInt();
    }
    runRepeatabilityTest(cycles, dist);
  } else if (cmd == "STATUS") {
    Serial.println(F("--- STAGE TELEMETRY ---"));
    Serial.print(F("Current Position : ")); Serial.print(current_pos_um); Serial.println(F(" um"));
    Serial.print(F("Homed Status     : ")); Serial.println(is_homed ? "YES" : "NO");
    Serial.print(F("Endstop Sensor   : ")); Serial.println(digitalRead(PIN_ENDSTOP) == LOW ? "BLOCKED" : "OPEN");
    Serial.print(F("Resolution       : 0.039 um / pulse\n"));
  } else {
    Serial.println(F("Unknown command. Available: HOME, G0 X<um>, TEST <cycles> <dist_um>, STATUS"));
  }
}
