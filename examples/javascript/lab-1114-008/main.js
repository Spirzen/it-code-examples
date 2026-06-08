let depth = 6;

function setup() {
  createCanvas(400, 400);
  background(173, 216, 230);
  angleMode(DEGREES);
  strokeWeight(2);

  push();
  translate(width / 2, height - 20);
  rotate(-90);
  drawTree(100, depth);
  pop();

  noLoop();
}

function drawTree(len, level) {
  if (level === 0) return;

  const brown = map(level, 0, depth, 100, 180);
  stroke(brown, 100, 50);
  line(0, 0, len, 0);
  translate(len, 0);

  push();
  rotate(30);
  drawTree(len * 0.7, level - 1);
  pop();

  push();
  rotate(-30);
  drawTree(len * 0.7, level - 1);
  pop();
}
