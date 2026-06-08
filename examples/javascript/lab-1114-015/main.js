function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);

  push();
  translate(width / 2, height / 2);
  drawRegularPolygon(5, 100);
  pop();

  noLoop();
}

function drawRegularPolygon(n, radius, doFill = false) {
  if (n < 3) return;
  stroke(0);
  strokeWeight(2);
  doFill ? fill(255, 200, 100) : noFill();

  beginShape();
  for (let i = 0; i < n; i++) {
    const a = -90 + (360 / n) * i;
    vertex(cos(a) * radius, sin(a) * radius);
  }
  endShape(CLOSE);
}
