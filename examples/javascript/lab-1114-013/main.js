function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);

  push();
  translate(width / 2, height / 2);
  drawEquilateralTriangle(100);
  pop();

  noLoop();
}

function drawEquilateralTriangle(side, doFill = false) {
  stroke(0);
  strokeWeight(2);
  doFill ? fill(100, 150, 255) : noFill();

  beginShape();
  for (let i = 0; i < 3; i++) {
    const a = -90 + i * 120;
    vertex(cos(a) * side, sin(a) * side);
  }
  endShape(CLOSE);
}
