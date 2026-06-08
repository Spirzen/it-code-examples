function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noStroke();
  fill(255, 150, 180);

  const petalCount = 10;
  const radius = 100;
  const petalR = 50;

  push();
  translate(width / 2, height / 2);
  for (let i = 0; i < petalCount; i++) {
    const a = radians(i * (360 / petalCount));
    circle(cos(a) * radius, sin(a) * radius, petalR * 2);
  }
  pop();

  noLoop();
}
