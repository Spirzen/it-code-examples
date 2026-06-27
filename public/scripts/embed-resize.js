(function () {
  var isEmbedPath = window.location.pathname.indexOf('/e/embed/') !== -1;
  var isLegacyEmbed = new URLSearchParams(window.location.search).get('embed') === '1';
  if (!isEmbedPath && !isLegacyEmbed) return;

  var postToParent =
    window.ITUParentOrigin && window.ITUParentOrigin.postToParent
      ? window.ITUParentOrigin.postToParent
      : function () {};

  var lastPosted = 0;
  var rafId = 0;

  function hideLoadingMask() {
    var mask = document.getElementById('embed-loading');
    if (mask) mask.hidden = true;
  }

  function measureHeight() {
    var root = document.querySelector('.embed-main') || document.querySelector('.file-tabs');
    if (root) {
      return Math.ceil(
        Math.max(root.scrollHeight, root.offsetHeight, root.getBoundingClientRect().height),
      );
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
    hideLoadingMask();
    postToParent({type: 'it-code-embed-height', height: height});
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
  [0, 120, 400, 1000, 2000].forEach(function (ms) {
    setTimeout(schedulePostHeight, ms);
  });
})();
