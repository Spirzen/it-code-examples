function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noFill();
  stroke(220, 30, 60);
  strokeWeight(3);

  push();
  translate(width / 2, height / 2);
  for (let i = 0; i < 6; i++) {
    circle(0, -30, 60);
    rotate(60);
  }
  noStroke();
  fill(255, 220, 0);
  circle(0, 0, 20);
  pop();

  noLoop();
}
