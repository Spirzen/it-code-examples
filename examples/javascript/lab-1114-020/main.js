function setup() {
  createCanvas(400, 400);
  background(20, 30, 60);
  angleMode(DEGREES);
  stroke(180, 220, 255);
  strokeWeight(1);

  const side = 200;
  push();
  translate(width / 2, height / 2 + side / 3);
  for (let i = 0; i < 3; i++) {
    kochSide(side, 4);
    rotate(120);
  }
  pop();

  noLoop();
}

function kochSide(len, depth) {
  if (depth === 0) {
    line(0, 0, len, 0);
    translate(len, 0);
    return;
  }
  const third = len / 3;
  kochSide(third, depth - 1);
  push();
  rotate(60);
  kochSide(third, depth - 1);
  pop();
  push();
  rotate(-60);
  kochSide(third, depth - 1);
  pop();
  kochSide(third, depth - 1);
}
