function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noStroke();
  fill(255, 182, 193);

  push();
  translate(width / 2, height / 2);
  for (let i = 0; i < 6; i++) {
    circle(0, -50, 100);
    rotate(60);
  }
  pop();

  noLoop();
}
