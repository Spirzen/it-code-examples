const int redPin = 8;
const int yellowPin = 9;
const int greenPin = 10;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void setLight(int r, int y, int g) {
  digitalWrite(redPin, r);
  digitalWrite(yellowPin, y);
  digitalWrite(greenPin, g);
}

void loop() {
  setLight(HIGH, LOW, LOW);
  delay(3000);
  setLight(HIGH, HIGH, LOW);
  delay(1000);
  setLight(LOW, LOW, HIGH);
  delay(3000);
  setLight(HIGH, HIGH, LOW);
  delay(1000);
}
