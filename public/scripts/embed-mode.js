(function () {
  var params = new URLSearchParams(window.location.search);
  if (params.get('embed') !== '1') return;

  var match = window.location.pathname.match(/\/e\/(.+?)\/?$/);
  if (match && match[1].indexOf('embed/') !== 0) {
    var target = '/e/embed/' + match[1].replace(/\/$/, '') + '/';
    window.location.replace(target + window.location.hash);
    return;
  }

  document.documentElement.classList.add('html--embed');

  function apply() {
    document.body.classList.add('site--embed');
    var article = document.querySelector('.example');
    if (article) article.classList.add('example--embed');
  }

  if (document.body) {
    apply();
  } else {
    document.addEventListener('DOMContentLoaded', apply);
  }
})();
