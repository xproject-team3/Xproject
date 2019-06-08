int Trig = 13;
int Echo = 12;
int led_R = 7;
int led_G = 6;
int led_B = 5;

void setup() {
  Serial.begin(9600);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
  pinMode(led_R, OUTPUT);
  pinMode(led_G, OUTPUT);
  pinMode(led_B, OUTPUT);
}

void loop() {
  digitalWrite(Trig, LOW);
  digitalWrite(Echo, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  
  unsigned long duration = pulseIn(Echo, HIGH);
  float distance = ((float)(340*duration) / 10000) / 2;
  
  Serial.println(distance);
  //Serial.println("cm");
  
  if(distance <= 5) {
    digitalWrite(led_R, HIGH);
    digitalWrite(led_G, LOW);
    digitalWrite(led_B, LOW);
  }
  else if(distance <= 10) {
    digitalWrite(led_R, LOW);
    digitalWrite(led_G, HIGH);
    digitalWrite(led_B, LOW);
  }
  else if(distance <= 15) {
    digitalWrite(led_R, LOW);
    digitalWrite(led_G, LOW);
    digitalWrite(led_B, HIGH);
  }
  else {
    digitalWrite(led_R, LOW);
    digitalWrite(led_G, LOW);
    digitalWrite(led_B, LOW);
  }
  
  delay(1000);
}
