showSlide(index) {
  this.slides.forEach((slide, i) => {
    const active = i === index;
    slide.dataset.active = active ? 'true' : 'false';
    slide.setAttribute('aria-hidden', active ? 'false' : 'true');
  });

  this.indicators.forEach((dot, i) => {
    const active = i === index;
    dot.dataset.active = active ? 'true' : 'false';
    if (active) {
      dot.setAttribute('aria-current', 'true');
    } else {
      dot.removeAttribute('aria-current');
    }
  });

  this.onSlideChange?.(index);
}
