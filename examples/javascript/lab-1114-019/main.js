function setup() {
  createCanvas(400, 400);
  background(240, 248, 255);
  angleMode(DEGREES);
  strokeWeight(2);

  push();
  translate(width / 2, height - 30);
  rotate(-90);
  pythagorasTree(80, 7);
  pop();

  noLoop();
}

function pythagorasTree(len, depth) {
  if (depth === 0) return;
  stroke(map(depth, 0, 7, 80, 40), 120, 60);
  line(0, 0, len, 0);
  translate(len, 0);

  push();
  rotate(35);
  pythagorasTree(len * 0.72, depth - 1);
  pop();

  push();
  rotate(-35);
  pythagorasTree(len * 0.72, depth - 1);
  pop();
}
