function turtleForward(len) {
  line(0, 0, len, 0);
  translate(len, 0);
}
function turtleLeft(deg) {
  rotate(deg);
}

function setup() {
  createCanvas(400, 400);
  background(240);
  angleMode(DEGREES);
  stroke(50);
  strokeWeight(2);
  fill(200, 180, 140);

  push();
  translate(width / 2 - 50, height / 2 + 50);

  for (let i = 0; i < 4; i++) {
    turtleLeft(90);
    turtleForward(100);
  }

  turtleLeft(45);
  turtleForward(70);
  turtleLeft(90);
  turtleForward(70);

  pop();
  noLoop();
}
