(function () {
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

  function copyText(text, btn, okLabel) {
    var label = btn.textContent;
    navigator.clipboard
      .writeText(text)
      .then(function () {
        btn.textContent = okLabel || 'Скопировано';
        btn.classList.add('is-copied');
        setTimeout(function () {
          btn.textContent = label;
          btn.classList.remove('is-copied');
        }, 1600);
      })
      .catch(function () {
        btn.textContent = 'Ошибка';
        setTimeout(function () {
          btn.textContent = label;
        }, 1600);
      });
  }

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

    var dialog = document.getElementById('code-fullscreen-dialog');
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.id = 'code-fullscreen-dialog';
      dialog.className = 'code-fullscreen-dialog';
      dialog.innerHTML =
        '<div class="code-fullscreen-dialog__inner">' +
        '<div class="code-fullscreen-dialog__toolbar">' +
        '<span class="code-fullscreen-dialog__title"></span>' +
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
      dialog.querySelector('[data-fs-copy]').addEventListener('click', function () {
        var body = dialog.querySelector('.code-fullscreen-dialog__body');
        var src = body.getAttribute('data-raw') || body.textContent || '';
        var btn = dialog.querySelector('[data-fs-copy]');
        copyText(src, btn);
      });
    }

    var title = block.getAttribute('data-filename') || 'Код';
    var body = dialog.querySelector('.code-fullscreen-dialog__body');
    var views = block.querySelector('.code-block__views');
    dialog.querySelector('.code-fullscreen-dialog__title').textContent = title;
    body.innerHTML = '';
    body.setAttribute('data-raw', block.getAttribute('data-raw') || '');
    if (views) {
      body.appendChild(views.cloneNode(true));
    } else {
      var pre = block.querySelector('pre');
      if (pre) {
        body.appendChild(pre.cloneNode(true));
      }
    }
    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      dialog.setAttribute('open', '');
    }
  });
})();
