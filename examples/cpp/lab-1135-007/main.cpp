const int buttonPin = 2;
const int ledPin = 13;

int ledState = LOW;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
}

void loop() {
  static int lastBtn = HIGH;
  int btn = digitalRead(buttonPin);

  if (lastBtn == HIGH && btn == LOW) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(50);
  }

  lastBtn = btn;
}
