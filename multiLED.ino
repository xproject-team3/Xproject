int Led_pin[5] = {2, 3, 4, 5, 6};

void setup() {
  for (int i = 0; i< 5; i++) {
    pinMode (Led_pin[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i< 5; i++) {
    digitalWrite(Led_pin[i], HIGH);
    delay(500);
  }
  for (int i = 4; i>=0; i--) {
    digitalWrite(Led_pin[i], LOW);
    delay(500);
  }
}
