/**
 * 4.18 — High-Level API: контекст, HiDPI, ввод
 * https://spirzen.ru/encyclopedia/4-code-dev/4-18-graphic-dev/6
 */

const LOGICAL_W = 400;
const LOGICAL_H = 260;

const canvas = document.getElementById('view');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
  const dpr = window.devicePixelRatio || 1;
  canvas.style.width = `${LOGICAL_W}px`;
  canvas.style.height = `${LOGICAL_H}px`;
  canvas.width = Math.round(LOGICAL_W * dpr);
  canvas.height = Math.round(LOGICAL_H * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// ─── Модель ───
const model = {
  pointer: { x: LOGICAL_W / 2, y: LOGICAL_H / 2 },
  camera: { x: 0, y: 0 },
};

// ─── Ввод: только запись в модель (не рисуем в handler!) ───
const keys = Object.create(null);

window.addEventListener('keydown', (e) => {
  keys[e.code] = true;
});
window.addEventListener('keyup', (e) => {
  keys[e.code] = false;
});

canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  const scaleX = LOGICAL_W / rect.width;
  const scaleY = LOGICAL_H / rect.height;
  model.pointer.x = (e.clientX - rect.left) * scaleX;
  model.pointer.y = (e.clientY - rect.top) * scaleY;
});

function update(dt) {
  const speed = 120;
  if (keys.ArrowLeft) model.camera.x -= speed * dt;
  if (keys.ArrowRight) model.camera.x += speed * dt;
  if (keys.ArrowUp) model.camera.y -= speed * dt;
  if (keys.ArrowDown) model.camera.y += speed * dt;
}

function render() {
  ctx.fillStyle = '#1e293b';
  ctx.fillRect(0, 0, LOGICAL_W, LOGICAL_H);

  ctx.save();
  ctx.translate(-model.camera.x, -model.camera.y);

  // сетка мира
  ctx.strokeStyle = '#334155';
  for (let x = 0; x < 800; x += 40) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, 400);
    ctx.stroke();
  }

  ctx.fillStyle = '#38bdf8';
  ctx.beginPath();
  ctx.arc(model.pointer.x, model.pointer.y, 14, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore();
}

let last = 0;
function loop(t) {
  const dt = last ? Math.min((t - last) / 1000, 0.05) : 0;
  last = t;
  update(dt);
  render();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
