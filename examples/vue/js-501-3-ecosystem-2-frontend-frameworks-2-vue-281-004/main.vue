<script setup>

import { ref, computed } from 'vue'

const items = ref(['Apple', 'Banana', 'Orange'])
const query = ref('')
const filtered = computed(() =>
  items.value.filter(i => i.toLowerCase().includes(query.value.toLowerCase()))
)
</script>

<template>
  <input v-model="query" placeholder="Поиск..." />
  <ul>
    <li v-for="item in filtered" :key="item">{{ item }}</li>
  </ul>
</template>
