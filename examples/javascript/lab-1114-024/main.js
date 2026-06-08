let t = 0;

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  background(20, 20, 40);
  stroke(100, 200, 255, 180);
  strokeWeight(1);
  noFill();

  push();
  translate(width / 2, height / 2);
  beginShape();
  for (let deg = 0; deg < 360 * 8; deg += 3) {
    const rad = radians(deg);
    const r = (5 + t * 0.5) + (2 + sin(t * 0.05)) * rad;
    vertex(cos(rad) * r, sin(rad) * r);
  }
  endShape();
  pop();

  t += 1;
}
