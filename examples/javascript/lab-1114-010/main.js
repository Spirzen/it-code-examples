function setup() {
  createCanvas(400, 400);
  background(255);
  noStroke();
  fill(0);

  const step = 25;
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const x = width / 2 - 100 + col * step;
      const y = height / 2 - 100 + row * step;
      circle(x, y, 12);
    }
  }

  noLoop();
}
