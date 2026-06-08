const video = document.getElementById('player');
const playBtn = document.getElementById('play');
const seek = document.getElementById('seek');

playBtn.addEventListener('click', () => {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
});

video.addEventListener('play', () => { playBtn.textContent = 'Пауза'; });
video.addEventListener('pause', () => { playBtn.textContent = 'Смотреть'; });

video.addEventListener('loadedmetadata', () => {
  seek.max = String(video.duration);
});

video.addEventListener('timeupdate', () => {
  if (!Number.isFinite(video.duration)) return;
  seek.value = String((video.currentTime / video.duration) * 100);
});

seek.addEventListener('input', () => {
  const ratio = Number(seek.value) / 100;
  video.currentTime = ratio * video.duration;
});
