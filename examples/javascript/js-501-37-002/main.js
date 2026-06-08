class SearchBox {
  constructor(root) {
    this.controller = null;
    this.root = root;
    this.root.querySelector('input').addEventListener('input', () => this.search());
  }

  search() {
    this.controller?.abort();
    this.controller = new AbortController();

    fetch(`/api/search?q=${encodeURIComponent(this.query)}`, {
      signal: this.controller.signal,
    })
      .then((r) => r.json())
      .then((items) => this.render(items))
      .catch((e) => {
        if (e.name !== 'AbortError') throw e;
      });
  }

  destroy() {
    this.controller?.abort();
  }
}
