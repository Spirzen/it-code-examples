/**
 * 4.18 — Структуры сцены: массив + culling
 * https://spirzen.ru/encyclopedia/4-code-dev/4-18-graphic-dev/4
 */

const W = 480;
const H = 320;

// ─── Модель: массив «строк таблицы» ───
const stars = Array.from({ length: 40 }, () => ({
  x: Math.random() * W * 1.4 - W * 0.2,
  y: Math.random() * H,
  r: 2 + Math.random() * 4,
  vx: (Math.random() - 0.5) * 80,
  removing: false,
}));

let cameraX = 0;

function update(dt) {
  cameraX += 60 * dt;
  for (const s of stars) {
    s.x += s.vx * dt;
    if (s.x < cameraX - 50 || s.x > cameraX + W + 50) s.removing = true;
  }
  // mark-and-sweep в конце кадра
  for (let i = stars.length - 1; i >= 0; i -= 1) {
    if (stars[i].removing) stars.splice(i, 1);
  }
}

/** 2D viewport culling — не рисуем то, что полностью за кадром */
function isVisible(s) {
  const sx = s.x - cameraX;
  return sx + s.r >= 0 && sx - s.r <= W;
}

function render(ctx) {
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = '#fbbf24';
  for (const s of stars) {
    if (!isVisible(s)) continue; // culling
    const sx = s.x - cameraX;
    ctx.beginPath();
    ctx.arc(sx, s.y, s.r, 0, Math.PI * 2);
    ctx.fill();
  }
  ctx.fillStyle = '#94a3b8';
  ctx.fillText(`objects: ${stars.length}`, 8, 18);
}

// Для встраивания в статью — экспорт логики (в браузере можно подключить к canvas)
if (typeof module !== 'undefined') {
  module.exports = { stars, update, isVisible, render, W, H };
}
