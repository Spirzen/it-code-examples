const int buzzerPin = 8;

#define NOTE_C4  262
#define NOTE_E4  330
#define NOTE_G4  392

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  tone(buzzerPin, NOTE_C4, 300);
  delay(350);
  tone(buzzerPin, NOTE_E4, 300);
  delay(350);
  tone(buzzerPin, NOTE_G4, 300);
  delay(600);
  noTone(buzzerPin);
  delay(1000);
}
