const int sensorPin = A0;
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  int ledBrightness = map(sensorValue, 0, 1023, 0, 255);

  analogWrite(ledPin, ledBrightness);

  Serial.print("Датчик: ");
  Serial.print(sensorValue);
  Serial.print("  Яркость: ");
  Serial.println(ledBrightness);

  delay(100);
}
