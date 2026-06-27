(function () {
  var FALLBACK_PARENT_ORIGINS = [
    'https://spirzen.ru',
    'https://www.spirzen.ru',
    'https://lab.spirzen.ru',
    'https://tools.spirzen.ru',
    'https://terms.spirzen.ru',
    'https://games.spirzen.ru',
    'https://kids.spirzen.ru',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3001',
    'http://localhost:4330',
    'http://localhost:4331',
    'http://localhost:4334',
  ];

  function isEmbeddedInParent() {
    try {
      return window.parent && window.parent !== window;
    } catch (e) {
      return true;
    }
  }

  function resolveParentOrigin() {
    if (!isEmbeddedInParent()) {
      return null;
    }
    try {
      return window.parent.location.origin;
    } catch (e) {
      if (document.referrer) {
        try {
          return new URL(document.referrer).origin;
        } catch (e2) {
          /* ignore */
        }
      }
    }
    return null;
  }

  function postToParent(message) {
    if (!isEmbeddedInParent()) {
      return;
    }
    var origin = resolveParentOrigin();
    if (origin) {
      try {
        window.parent.postMessage(message, origin);
      } catch (e) {
        /* ignore */
      }
      return;
    }
    FALLBACK_PARENT_ORIGINS.forEach(function (fallbackOrigin) {
      try {
        window.parent.postMessage(message, fallbackOrigin);
      } catch (e) {
        /* ignore */
      }
    });
  }

  window.ITUParentOrigin = {
    postToParent: postToParent,
    resolveParentOrigin: resolveParentOrigin,
    isEmbeddedInParent: isEmbeddedInParent,
  };
})();
