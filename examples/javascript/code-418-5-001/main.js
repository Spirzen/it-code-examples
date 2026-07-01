/**
 * 4.18 — Математика 2D для графики
 * https://spirzen.ru/encyclopedia/4-code-dev/4-18-graphic-dev/5
 */

const Vec2 = {
  add(a, b) {
    return { x: a.x + b.x, y: a.y + b.y };
  },
  sub(a, b) {
    return { x: a.x - b.x, y: a.y - b.y };
  },
  scale(v, k) {
    return { x: v.x * k, y: v.y * k };
  },
  len(v) {
    return Math.hypot(v.x, v.y);
  },
  norm(v) {
    const l = Vec2.len(v) || 1;
    return { x: v.x / l, y: v.y / l };
  },
  dot(a, b) {
    return a.x * b.x + a.y * b.y;
  },
  /** Поворот вектора на угол θ (радианы) */
  rotate(v, theta) {
    const c = Math.cos(theta);
    const s = Math.sin(theta);
    return { x: v.x * c - v.y * s, y: v.x * s + v.y * c };
  },
  lerp(a, b, t) {
    return { x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t };
  },
};

function circlesOverlap(a, b) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const distSq = dx * dx + dy * dy;
  const r = a.radius + b.radius;
  return distSq < r * r;
}

// Пример: враг «видит» игрока, если угол < 45°
function isFacing(enemy, player) {
  const toPlayer = Vec2.norm(Vec2.sub(player, enemy));
  const forward = Vec2.rotate({ x: 1, y: 0 }, enemy.angle);
  const cosLimit = Math.cos((45 * Math.PI) / 180);
  return Vec2.dot(forward, toPlayer) > cosLimit;
}

// Демо-вызовы для каталога кода
const player = { x: 100, y: 100, radius: 12 };
const enemy = { x: 130, y: 100, radius: 10, angle: 0 };
console.log('overlap', circlesOverlap(player, enemy));
console.log('facing', isFacing(enemy, player));
console.log('rotated', Vec2.rotate({ x: 10, y: 0 }, Math.PI / 2));
