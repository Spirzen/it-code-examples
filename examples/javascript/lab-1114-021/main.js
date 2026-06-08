function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  stroke(0);
  strokeWeight(1);
  noFill();

  push();
  translate(width / 2, height / 2);
  beginShape();
  for (let deg = 0; deg < 360 * 5; deg += 2) {
    const rad = radians(deg);
    const r = 5 + 2 * rad;
    vertex(cos(rad) * r, sin(rad) * r);
  }
  endShape();
  pop();

  noLoop();
}
