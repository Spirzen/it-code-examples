<script setup>

import { ref, onMounted } from 'vue'

const notes = ref([])
const error = ref('')
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await fetch('http://127.0.0.1:3000/notes')
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    notes.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section>
    <h2>Заметки с сервера</h2>
    <p v-if="loading">Загрузка…</p>
    <p v-else-if="error">Ошибка: {{ error }}</p>
    <ul v-else>
      <li v-for="n in notes" :key="n.id">{{ n.text }}</li>
    </ul>
  </section>
</template>
