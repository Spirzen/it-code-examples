function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);

  push();
  translate(width / 2, height / 2);
  drawStar(5, 100, 40);
  pop();

  noLoop();
}

function drawStar(points, outerR, innerR, doFill = false) {
  stroke(0);
  strokeWeight(2);
  doFill ? fill(255, 215, 0) : noFill();

  beginShape();
  for (let i = 0; i < points * 2; i++) {
    const r = i % 2 === 0 ? outerR : innerR;
    const a = -90 + (180 / points) * i;
    vertex(cos(a) * r, sin(a) * r);
  }
  endShape(CLOSE);
}
