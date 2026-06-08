class UserCard extends HTMLElement {
  connectedCallback() {
    if (this._ready) return;
    this._ready = true;

    const name = this.getAttribute('name') ?? 'Гость';
    this.innerHTML = `
      <article class="user-card">
        <h2>${escapeHtml(name)}</h2>
        <slot></slot>
      </article>
`;
  }

  static get observedAttributes() {
    return ['name'];
  }

  attributeChangedCallback(attr, oldVal, newVal) {
    if (attr === 'name' && oldVal !== newVal) {
      this._ready = false;
      this.connectedCallback();
    }
  }
}

function escapeHtml(text) {
  return text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

customElements.define('user-card', UserCard);
