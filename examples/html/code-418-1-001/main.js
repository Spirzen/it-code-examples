/**
 * Энциклопедия 4.18 — От чисел к картинке
 * https://spirzen.ru/encyclopedia/4-code-dev/4-18-graphic-dev/1
 */

const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const W = canvas.width;
const H = canvas.height;

// ─── 1. МОДЕЛЬ (только числа в памяти, экран не трогаем) ───
const ball = {
  x: W / 2,
  y: H / 2,
  vx: 140,
  vy: 95,
  radius: 18,
  color: '#ef4444',
};

// ─── 2. UPDATE — меняем модель по правилам игры ───
function update(dt) {
  ball.x += ball.vx * dt;
  ball.y += ball.vy * dt;

  const r = ball.radius;
  if (ball.x < r || ball.x > W - r) {
    ball.x = Math.max(r, Math.min(W - r, ball.x));
    ball.vx *= -1;
  }
  if (ball.y < r || ball.y > H - r) {
    ball.y = Math.max(r, Math.min(H - r, ball.y));
    ball.vy *= -1;
  }
}

// ─── 3. RENDER — читаем модель, команды «художнику» ───
function render() {
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, W, H);

  ctx.fillStyle = ball.color;
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fill();
}

// ─── 4. ИГРОВОЙ ЦИКЛ (~60 FPS) ───
let lastTime = 0;

function loop(timestamp) {
  const dt = lastTime ? Math.min((timestamp - lastTime) / 1000, 0.05) : 0;
  lastTime = timestamp;

  update(dt);
  render();

  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);
