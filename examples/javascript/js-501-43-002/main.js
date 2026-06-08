class StatusBadge extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    shadow.innerHTML = `
      <style>
        :host {
          display: inline-block;
          font: 14px/1.4 system-ui, sans-serif;
        }
        .badge {
          padding: 2px 8px;
          border-radius: 999px;
          background: var(--badge-bg, #e0e0e0);
        }
      </style>
      <span class="badge"><slot></slot></span>
`;
  }
}

customElements.define('status-badge', StatusBadge);
