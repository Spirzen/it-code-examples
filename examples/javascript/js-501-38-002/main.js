const sentinel = document.querySelector('#list-sentinel');
let loading = false;

const listObserver = new IntersectionObserver(async (entries) => {
  const visible = entries.some((e) => e.isIntersecting);
  if (!visible || loading) return;

  loading = true;
  try {
    const chunk = await loadNextPage();
    appendItems(chunk);
  } finally {
    loading = false;
  }
});

listObserver.observe(sentinel);
