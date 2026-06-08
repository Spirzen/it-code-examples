function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  stroke(180, 50, 150);
  strokeWeight(2);
  noFill();

  const k = 5;
  const a = 100;

  push();
  translate(width / 2, height / 2);
  beginShape();
  const steps = k % 2 === 0 ? 720 : 360;
  for (let deg = 0; deg <= steps; deg += 2) {
    const rad = radians(deg);
    const r = a * cos(k * rad);
    vertex(cos(rad) * r, sin(rad) * r);
  }
  endShape();
  pop();

  noLoop();
}
