(function () {
  document.addEventListener('click', function (event) {
    var btn = event.target.closest('[data-copy]');
    if (!btn) return;

    var block = btn.closest('.code-block');
    var pre = block && block.querySelector('pre');
    if (!pre) return;

    var text = pre.textContent || '';
    if (!text) return;

    var label = btn.textContent;
    navigator.clipboard
      .writeText(text)
      .then(function () {
        btn.textContent = 'Скопировано';
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
  });
})();
