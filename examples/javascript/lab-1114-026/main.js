function setup() {
  createCanvas(800, 600);
  angleMode(DEGREES);
  pixelDensity(1);
  background(255);

  drawScene();

  noLoop();
}

function draw() {
  // анимация: уберите noLoop() и перенесите drawScene() сюда
}

function drawScene() {
  push();
  translate(width / 2, height / 2);
  // ваши фигуры
  pop();
}
