function setup() {
  createCanvas(400, 400);
  background(255);
  noStroke();

  const size = 30;
  const startX = width / 2 - 120;
  const startY = height / 2 - 120;

  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const x = startX + col * size;
      const y = startY + row * size;
      fill((row + col) % 2 === 0 ? 0 : 255);
      circle(x + size / 2, y + size / 2, size);
    }
  }

  noLoop();
}
