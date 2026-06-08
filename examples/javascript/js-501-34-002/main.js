createIndicators() {
  if (!this.indicatorsHost) return;

  this.indicatorsHost.innerHTML = '';
  this.indicators = [];

  for (let i = 0; i < this.slideCount; i++) {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('data-carousel-dot', '');
    dot.setAttribute('aria-label', `Слайд ${i + 1}`);

    dot.addEventListener('click', () => {
      this.goToSlide(i);
      this.resetAutoplay();
    });

    this.indicatorsHost.appendChild(dot);
    this.indicators.push(dot);
  }
}
