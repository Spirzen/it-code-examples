function setup() {
  createCanvas(400, 400);
  background(255);

  push();
  translate(width / 2, height / 2);
  drawRectangle(100, 200);
  pop();

  noLoop();
}

function drawRectangle(w, h, doFill = false) {
  stroke(0);
  strokeWeight(2);
  doFill ? fill(180, 200, 255) : noFill();
  rectMode(CENTER);
  rect(0, 0, w, h);
}
