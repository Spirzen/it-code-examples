function setup() {
  createCanvas(500, 400);
  background(255);
  angleMode(DEGREES);
  stroke(200, 160, 0);
  strokeWeight(1);
  noFill();

  const r = 25;
  const cols = 8;
  const rows = 6;
  const dx = r * 3;
  const dy = r * sqrt(3);

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const x = 60 + col * dx + (row % 2) * (dx / 2);
      const y = 50 + row * dy;
      drawHex(x, y, r);
    }
  }

  noLoop();
}

function drawHex(cx, cy, radius) {
  push();
  translate(cx, cy);
  beginShape();
  for (let i = 0; i < 6; i++) {
    const a = 30 + i * 60;
    vertex(cos(a) * radius, sin(a) * radius);
  }
  endShape(CLOSE);
  pop();
}
