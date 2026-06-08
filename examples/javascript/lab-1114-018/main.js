function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  noFill();
  stroke(255, 105, 180);
  strokeWeight(2);

  push();
  translate(width / 2, height / 2);
  drawRose(5, 80);
  pop();

  noLoop();
}

function drawRose(petalCount, radius) {
  for (let i = 0; i < petalCount; i++) {
    push();
    rotate(i * (360 / petalCount));
    arc(0, -radius / 2, radius, radius, -60, 60);
    pop();
  }
}
