// stores/notes.js
import { defineStore } from 'pinia';

export const useNotesStore = defineStore('notes', {
  state: () => ({ items: [], loading: false }),
  actions: {
    async fetchAll() {
      this.loading = true;
      const res = await fetch('http://127.0.0.1:3000/notes');
      this.items = await res.json();
      this.loading = false;
    },
  },
});
