function turtleForward(len) {
  line(0, 0, len, 0);
  translate(len, 0);
}
function turtleLeft(deg) {
  rotate(deg);
}

function setup() {
  createCanvas(400, 400);
  background(255);
  angleMode(DEGREES);
  stroke(0);
  strokeWeight(2);
  noFill();

  push();
  translate(width / 2, height / 2);
  for (let i = 0; i < 4; i++) {
    turtleForward(100);
    turtleLeft(90);
  }
  pop();

  noLoop();
}
