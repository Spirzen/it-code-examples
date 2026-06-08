ctx.beginPath();
ctx.moveTo(20, 20);
ctx.lineTo(100, 20);
ctx.lineTo(100, 80);
ctx.closePath();
ctx.strokeStyle = 'rgb(255, 0, 0)';
ctx.lineWidth = 3;
ctx.stroke();
ctx.fillStyle = 'rgb(0, 0, 255)';
ctx.fill();

ctx.beginPath();
ctx.arc(200, 150, 100, 0, Math.PI * 2);
ctx.stroke();
