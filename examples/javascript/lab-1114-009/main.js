function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noStroke();
  fill(220, 30, 60);

  push();
  translate(width / 2, height / 2 + 20);
  rotate(-50);
  beginShape();
  vertex(0, 0);
  bezierVertex(0, -50, 100, -50, 100, 0);
  bezierVertex(100, 50, 0, 80, 0, 0);
  endShape(CLOSE);
  pop();

  noLoop();
}
