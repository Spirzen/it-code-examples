const DEFAULT_AUTOPLAY_MS = 5000;

class PromoCarousel {
  constructor({ root, autoplayDelay = DEFAULT_AUTOPLAY_MS, onSlideChange } = {}) {
    if (!root) {
      throw new Error('PromoCarousel: нужен корневой элемент');
    }

    this.root = root;
    this.slides = [...root.querySelectorAll('[data-carousel-slide]')];
    this.prevBtn = root.querySelector('[data-carousel-prev]');
    this.nextBtn = root.querySelector('[data-carousel-next]');
    this.indicatorsHost = root.querySelector('[data-carousel-indicators]');

    this.currentIndex = 0;
    this.slideCount = this.slides.length;
    this.autoplayDelay = autoplayDelay;
    this.autoplayInterval = null;
    this.onSlideChange = onSlideChange;
    this.indicators = [];

    if (this.slideCount === 0) {
      return;
    }

    this.init();
  }

  init() {
    this.createIndicators();
    this.showSlide(this.currentIndex);
    this.startAutoplay();
    this.bindControls();
    this.bindHoverPause();
  }

  // ... методы ниже разобраны по блокам
}
