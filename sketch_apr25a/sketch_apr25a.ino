void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // Use pin 13 for LED
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    digitalWrite(13, cmd == '1' ? HIGH : LOW);
  }
}
