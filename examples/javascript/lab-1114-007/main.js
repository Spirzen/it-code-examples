function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noStroke();

  push();
  translate(width / 2, height / 2);

  fill(173, 216, 230);
  for (let i = 0; i < 12; i++) {
    arcLeaf(80, 60);
    rotate(30);
  }

  fill(144, 238, 144);
  for (let i = 0; i < 8; i++) {
    arcLeaf(60, 60);
    rotate(45);
  }

  fill(255, 220, 0);
  circle(0, 0, 30);

  pop();
  noLoop();
}

function arcLeaf(r, spread) {
  beginShape();
  vertex(0, 0);
  bezierVertex(r, -spread, r, spread, 0, 0);
  endShape(CLOSE);
}
