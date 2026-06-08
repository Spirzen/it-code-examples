(function () {
  var PAGE_SIZE = 48;
  var root = document.querySelector('[data-catalog]');
  if (!root) return;

  var base = root.getAttribute('data-base') || '/';
  var catalogUrl = root.getAttribute('data-catalog-url') || base + 'catalog.json';
  var languageFilter = root.getAttribute('data-language') || '';
  var languageLabel = root.getAttribute('data-language-label') || '';

  var input = root.querySelector('[data-search-input]');
  var grid = root.querySelector('[data-catalog-grid]');
  var empty = root.querySelector('[data-search-empty]');
  var countEl = root.querySelector('[data-search-count]');
  var loadMoreWrap = root.querySelector('[data-load-more-wrap]');
  var loadMoreBtn = root.querySelector('[data-load-more]');
  var loadMoreMeta = root.querySelector('[data-load-more-meta]');
  var searchResults = root.querySelector('[data-search-results]');
  var langGrid = root.querySelector('[data-lang-grid]');

  var catalog = null;
  var filtered = [];
  var rendered = 0;
  var query = '';

  function sitePath(path) {
    var normalized = (path || '').replace(/^\//, '');
    return base + normalized;
  }

  function normalize(value) {
    return (value || '').toLowerCase().trim();
  }

  function matchesQuery(item, q) {
    if (!q) return true;
    var haystack = [
      item.title,
      item.description,
      item.slug,
      item.language,
      (item.tags || []).join(' '),
      item.seriesTitle || item.series || '',
    ]
      .map(normalize)
      .join(' ');
    return haystack.indexOf(q) !== -1;
  }

  function escapeHtml(text) {
    return String(text || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderCard(item) {
    var li = document.createElement('li');
    li.className = 'example-card';
    li.setAttribute('data-slug', item.slug);

    var tags = (item.tags || []).slice(0, 2);
    var tagsHtml = tags.map(function (tag) {
      return '<span class="tag">' + escapeHtml(tag) + '</span>';
    }).join('');

    var seriesHtml = item.series
      ? '<span class="tag tag--series">' + escapeHtml(item.seriesTitle || item.series) + '</span>'
      : '';
    var filesHtml = item.fileCount > 1
      ? '<span class="tag tag--muted">' + item.fileCount + ' файла</span>'
      : '';
    var diffHtml = item.versionCount >= 2 ? '<span class="tag tag--muted">diff</span>' : '';
    var descHtml = item.description
      ? '<span class="example-card__desc">' + escapeHtml(item.description) + '</span>'
      : '';

    li.innerHTML =
      '<a class="example-card__link" href="' +
      escapeHtml(sitePath('e/' + item.slug + '/')) +
      '">' +
      '<span class="example-card__title">' +
      escapeHtml(item.title) +
      '</span>' +
      descHtml +
      '</a>' +
      '<div class="example-card__foot">' +
      seriesHtml +
      tagsHtml +
      filesHtml +
      diffHtml +
      '</div>';

    return li;
  }

  function applyFilter() {
    query = input ? normalize(input.value) : '';

    if (!languageFilter && !query) {
      if (grid) grid.innerHTML = '';
      if (langGrid) langGrid.hidden = false;
      if (searchResults) searchResults.hidden = true;
      if (loadMoreWrap) loadMoreWrap.hidden = true;
      if (empty) empty.hidden = true;
      if (countEl) countEl.textContent = '';
      return;
    }

    filtered = catalog.filter(function (item) {
      var langOk = !languageFilter || item.language === languageFilter;
      return langOk && matchesQuery(item, query);
    });
    rendered = 0;
    if (grid) grid.innerHTML = '';
    renderBatch();

    if (langGrid) langGrid.hidden = !!query;
    if (searchResults) searchResults.hidden = !query;

    if (empty) empty.hidden = filtered.length !== 0;
    updateCount();
  }

  function renderBatch() {
    if (!grid) return;
    var next = filtered.slice(rendered, rendered + PAGE_SIZE);
    next.forEach(function (item) {
      grid.appendChild(renderCard(item));
    });
    rendered += next.length;
    updateLoadMore();
  }

  function updateCount() {
    if (!countEl) return;
    if (query || languageFilter) {
      countEl.textContent = 'Показано: ' + Math.min(rendered, filtered.length) + ' из ' + filtered.length;
    } else if (rendered < filtered.length) {
      countEl.textContent = 'Показано: ' + rendered + ' из ' + filtered.length;
    } else {
      countEl.textContent = '';
    }
  }

  function updateLoadMore() {
    if (!loadMoreWrap || !loadMoreBtn) return;
    var hasMore = rendered < filtered.length;
    loadMoreWrap.hidden = !hasMore || filtered.length === 0;
    if (loadMoreMeta) {
      loadMoreMeta.textContent = hasMore
        ? rendered + ' из ' + filtered.length
        : '';
    }
    updateCount();
  }

  function fetchCatalog() {
    return fetch(catalogUrl).then(function (res) {
      if (!res.ok) throw new Error('catalog fetch failed');
      return res.json();
    });
  }

  function initLangGrid() {
    if (!langGrid || !catalog) return;
    var counts = {};
    catalog.forEach(function (item) {
      counts[item.language] = (counts[item.language] || 0) + 1;
    });
    var cards = langGrid.querySelectorAll('[data-lang-card]');
    cards.forEach(function (card) {
      var lang = card.getAttribute('data-lang-card');
      var countNode = card.querySelector('[data-lang-count]');
      if (countNode && counts[lang]) {
        countNode.textContent = counts[lang];
      }
    });
  }

  fetchCatalog()
    .then(function (data) {
      catalog = data;
      initLangGrid();
      applyFilter();
    })
    .catch(function () {
      if (empty) {
        empty.hidden = false;
        empty.textContent = 'Не удалось загрузить каталог. Обновите страницу.';
      }
    });

  if (input) {
    input.addEventListener('input', applyFilter);
  }

  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', renderBatch);
  }
})();
