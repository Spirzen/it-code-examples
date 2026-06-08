startAutoplay() {
  if (this.slideCount <= 1) return;
  if (window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches) return;

  this.stopAutoplay();
  this.autoplayInterval = window.setInterval(() => this.next(), this.autoplayDelay);
}

stopAutoplay() {
  if (this.autoplayInterval) {
    window.clearInterval(this.autoplayInterval);
    this.autoplayInterval = null;
  }
}

resetAutoplay() {
  this.stopAutoplay();
  this.startAutoplay();
}
