function setup() {
  createCanvas(400, 400);
  background(255);
  stroke(0);
  strokeWeight(1);
  noFill();

  const step = 30;
  const startX = width / 2 - 50;
  const startY = height / 2 - 50;

  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 3; col++) {
      const x = startX + col * step;
      const y = startY + row * step;
      rect(x, y, 20, 20);
    }
  }

  noLoop();
}
