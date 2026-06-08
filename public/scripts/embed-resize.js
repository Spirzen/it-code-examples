(function () {
  var isEmbedPath = window.location.pathname.indexOf('/e/embed/') !== -1;
  var isLegacyEmbed = new URLSearchParams(window.location.search).get('embed') === '1';
  if (!isEmbedPath && !isLegacyEmbed) return;

  var allowed = [
    'https://spirzen.ru',
    'https://www.spirzen.ru',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3001',
  ];

  var lastPosted = 0;
  var rafId = 0;

  function measureHeight() {
    var root = document.querySelector('.embed-main') || document.querySelector('.file-tabs');
    if (root) {
      return Math.ceil(root.getBoundingClientRect().height);
    }
    return Math.ceil(document.documentElement.offsetHeight);
  }

  function postHeightNow() {
    rafId = 0;
    var height = Math.max(measureHeight(), 80);
    if (Math.abs(height - lastPosted) < 2) {
      return;
    }
    lastPosted = height;
    if (window.parent && window.parent !== window) {
      allowed.forEach(function (origin) {
        try {
          window.parent.postMessage({type: 'it-code-embed-height', height: height}, origin);
        } catch (e) {
          /* ignore */
        }
      });
    }
  }

  function schedulePostHeight() {
    if (rafId) return;
    rafId = requestAnimationFrame(postHeightNow);
  }

  window.addEventListener('load', schedulePostHeight);
  window.addEventListener('resize', schedulePostHeight);
  if (typeof ResizeObserver !== 'undefined') {
    var root = document.querySelector('.embed-main') || document.querySelector('.file-tabs');
    new ResizeObserver(schedulePostHeight).observe(root || document.body);
  }
  [0, 120, 400, 1000].forEach(function (ms) {
    setTimeout(schedulePostHeight, ms);
  });
})();
