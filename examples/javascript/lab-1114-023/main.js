let angle = 0;

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  background(255);
  noFill();
  stroke(255, 105, 180);
  strokeWeight(2);

  push();
  translate(width / 2, height / 2);
  rotate(angle);
  drawRose(6, 80);
  pop();

  angle += 2;
}

function drawRose(petalCount, radius) {
  for (let i = 0; i < petalCount; i++) {
    push();
    rotate(i * (360 / petalCount));
    arc(0, -radius / 2, radius, radius, -60, 60);
    pop();
  }
}
