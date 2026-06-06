const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d');
const button = document.getElementById('draw');

button.addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#6ea1ff';
  ctx.fillRect(24, 24, 120, 64);
  ctx.fillStyle = '#9aa6ba';
  ctx.font = '14px Segoe UI, sans-serif';
  ctx.fillText('IT Code Examples', 24, 120);
});
