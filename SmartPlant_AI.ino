
const int soilPin = A0;
const int greenLED = 8;
const int redLED = 9;
const int buzzer = 10;

// Provisional thresholds: calibrate using your actual sensor.
const int DRY_THRESHOLD = 700;
const int CRITICAL_THRESHOLD = 820;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  int soilValue = analogRead(soilPin);
  int baselineState;

  if (soilValue >= CRITICAL_THRESHOLD) {
    baselineState = 2;  // critical_dry

    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);
    digitalWrite(buzzer, HIGH);

  } else if (soilValue >= DRY_THRESHOLD) {
    baselineState = 1;  // dry

    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);
    digitalWrite(buzzer, LOW);

  } else {
    baselineState = 0;  // moist

    digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);
    digitalWrite(buzzer, LOW);
  }

  // Send sensor data to Python:
  // P1,timestamp_ms,raw_value,baseline_state
  Serial.print("P1,");
  Serial.print(millis());
  Serial.print(",");
  Serial.print(soilValue);
  Serial.print(",");
  Serial.println(baselineState);

  delay(500);
}
