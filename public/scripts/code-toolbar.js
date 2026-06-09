(function () {
  var EMBED_ORIGINS = [
    'https://spirzen.ru',
    'https://www.spirzen.ru',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3001',
  ];

  function isEmbedContext() {
    return (
      window.location.pathname.indexOf('/e/embed/') !== -1 ||
      new URLSearchParams(window.location.search).get('embed') === '1'
    );
  }

  function postToParent(payload) {
    if (!window.parent || window.parent === window) return;
    EMBED_ORIGINS.forEach(function (origin) {
      try {
        window.parent.postMessage(payload, origin);
      } catch (e) {
        /* ignore */
      }
    });
  }

  function notifyEmbedHeight() {
    if (!isEmbedContext()) return;
    var root = document.querySelector('.embed-main') || document.querySelector('.file-tabs');
    var height = root
      ? Math.ceil(root.getBoundingClientRect().height)
      : Math.ceil(document.documentElement.offsetHeight);
    postToParent({type: 'it-code-embed-height', height: Math.max(height, 80)});
  }

  function postFullscreen(active, extra) {
    if (!isEmbedContext()) return;
    var payload = {type: 'it-code-fullscreen', active: active};
    if (extra) {
      Object.keys(extra).forEach(function (key) {
        payload[key] = extra[key];
      });
    }
    postToParent(payload);
  }

  function getVisiblePre(block) {
    var views = block.querySelector('.code-block__views');
    if (!views) {
      return block.querySelector('pre');
    }
    var dark = views.querySelector('.code-block__view--dark');
    var light = views.querySelector('.code-block__view--light');
    var theme = document.documentElement.getAttribute('data-theme');
    if (theme === 'light' && light) {
      return light.querySelector('pre');
    }
    if (theme === 'dark' && dark) {
      return dark.querySelector('pre');
    }
    var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var active = prefersDark ? dark : light;
    return (active || dark || light).querySelector('pre');
  }

  function getRawText(block) {
    var raw = block.getAttribute('data-raw');
    if (raw) return raw;
    var pre = getVisiblePre(block);
    return pre ? pre.textContent || '' : '';
  }

  function buildBlockTitle(block) {
    var langLabel = block.getAttribute('data-lang-label') || '';
    var filename = block.getAttribute('data-filename') || '';
    var parts = [langLabel, filename].filter(Boolean);
    return parts.length ? parts.join(' · ') : 'Код';
  }

  function copyWithExecCommand(text) {
    try {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;left:-9999px;top:0;opacity:0;pointer-events:none';
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      var ok = document.execCommand('copy');
      document.body.removeChild(ta);
      return ok;
    } catch (e) {
      return false;
    }
  }

  function copyViaParent(text) {
    return new Promise(function (resolve) {
      if (!isEmbedContext() || window.parent === window) {
        resolve(false);
        return;
      }
      var id = 'copy-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
      var settled = false;

      function finish(ok) {
        if (settled) return;
        settled = true;
        window.removeEventListener('message', onMessage);
        clearTimeout(timer);
        resolve(Boolean(ok));
      }

      function onMessage(event) {
        var data = event.data;
        if (!data || data.type !== 'it-code-copy-result' || data.id !== id) return;
        finish(data.ok);
      }

      var timer = setTimeout(function () {
        finish(false);
      }, 2000);

      window.addEventListener('message', onMessage);
      postToParent({type: 'it-code-copy', id: id, text: text});
    });
  }

  function copyText(text, btn, okLabel) {
    var label = btn.textContent;

    function onSuccess() {
      btn.textContent = okLabel || 'Скопировано';
      btn.classList.add('is-copied');
      setTimeout(function () {
        btn.textContent = label;
        btn.classList.remove('is-copied');
      }, 1600);
    }

    function onError() {
      btn.textContent = 'Ошибка';
      setTimeout(function () {
        btn.textContent = label;
      }, 1600);
    }

    function attempt() {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        return navigator.clipboard.writeText(text).catch(function () {
          if (copyWithExecCommand(text)) return;
          if (isEmbedContext()) return copyViaParent(text);
          throw new Error('copy failed');
        });
      }
      if (copyWithExecCommand(text)) return Promise.resolve();
      if (isEmbedContext()) return copyViaParent(text);
      return Promise.reject(new Error('copy failed'));
    }

    attempt().then(onSuccess).catch(onError);
  }

  var dialog = null;

  function ensureDialog() {
    if (dialog) return dialog;

    dialog = document.createElement('dialog');
    dialog.id = 'code-fullscreen-dialog';
    dialog.className = 'code-fullscreen-dialog';
    dialog.innerHTML =
      '<div class="code-fullscreen-dialog__inner">' +
      '<div class="code-fullscreen-dialog__toolbar">' +
      '<div class="code-fullscreen-dialog__meta">' +
      '<span class="code-fullscreen-dialog__lang"></span>' +
      '<span class="code-fullscreen-dialog__title"></span>' +
      '</div>' +
      '<div class="code-fullscreen-dialog__actions">' +
      '<button type="button" class="code-block__btn" data-fs-copy>Копировать</button>' +
      '<button type="button" class="code-block__btn" data-fs-close>Закрыть</button>' +
      '</div></div>' +
      '<div class="code-fullscreen-dialog__body"></div></div>';
    document.body.appendChild(dialog);

    dialog.querySelector('[data-fs-close]').addEventListener('click', function () {
      dialog.close();
    });
    dialog.addEventListener('click', function (e) {
      if (e.target === dialog) dialog.close();
    });
    dialog.addEventListener('close', function () {
      postFullscreen(false);
      notifyEmbedHeight();
    });
    dialog.querySelector('[data-fs-copy]').addEventListener('click', function () {
      var body = dialog.querySelector('.code-fullscreen-dialog__body');
      var src = body.getAttribute('data-raw') || '';
      var btn = dialog.querySelector('[data-fs-copy]');
      copyText(src, btn);
    });

    return dialog;
  }

  window.addEventListener('message', function (event) {
    if (!event.data || event.data.type !== 'it-code-fullscreen-close') return;
    var openDialog = document.getElementById('code-fullscreen-dialog');
    if (openDialog && openDialog.open) {
      openDialog.close();
    }
  });

  document.addEventListener('click', function (event) {
    var copyBtn = event.target.closest('[data-copy]');
    if (copyBtn) {
      var block = copyBtn.closest('.code-block') || copyBtn.closest('.embed-help');
      if (!block) return;
      var text = getRawText(block);
      if (!text) return;
      copyText(text, copyBtn);
      return;
    }

    var copyAllBtn = event.target.closest('[data-copy-all]');
    if (copyAllBtn) {
      var sources = copyAllBtn.getAttribute('data-sources') || '';
      if (!sources) return;
      copyText(sources, copyAllBtn, 'Все скопированы');
      return;
    }

    var fsBtn = event.target.closest('[data-fullscreen]');
    if (!fsBtn) return;

    var block = fsBtn.closest('.code-block');
    if (!block) return;

    var dlg = ensureDialog();
    var langLabel = block.getAttribute('data-lang-label') || '';
    var filename = block.getAttribute('data-filename') || '';
    var body = dlg.querySelector('.code-fullscreen-dialog__body');
    var langEl = dlg.querySelector('.code-fullscreen-dialog__lang');
    var titleEl = dlg.querySelector('.code-fullscreen-dialog__title');

    langEl.textContent = langLabel;
    langEl.hidden = !langLabel;
    titleEl.textContent = filename;
    titleEl.hidden = !filename;

    body.innerHTML = '';
    body.setAttribute('data-raw', block.getAttribute('data-raw') || '');

    var pre = getVisiblePre(block);
    if (pre) {
      var wrap = document.createElement('div');
      wrap.className = 'code-fullscreen-dialog__code';
      wrap.appendChild(pre.cloneNode(true));
      body.appendChild(wrap);
    }

    if (typeof dlg.showModal === 'function') {
      dlg.showModal();
    } else {
      dlg.setAttribute('open', '');
    }

    postFullscreen(true, {title: buildBlockTitle(block)});
    notifyEmbedHeight();
  });
})();
