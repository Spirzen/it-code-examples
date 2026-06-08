function setup() {
  createCanvas(400, 400);
  background(20, 30, 50);
  angleMode(DEGREES);
  stroke(100, 220, 255);
  strokeWeight(2);

  push();
  translate(width / 2, height / 2);
  for (let i = 0; i < 8; i++) {
    line(0, 0, 50, 0);
    rotate(45);
  }
  pop();

  noLoop();
}
