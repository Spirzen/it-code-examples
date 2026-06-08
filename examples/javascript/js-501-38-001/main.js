const images = document.querySelectorAll('img[data-src]');

const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;

      const img = entry.target;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      observer.unobserve(img);
    }
  },
  {
    root: null,       // viewport
    rootMargin: '200px 0px', // подгрузить чуть раньше появления
    threshold: 0.01,  // доля видимой площади (0…1 или массив)
  }
);

images.forEach((img) => observer.observe(img));
