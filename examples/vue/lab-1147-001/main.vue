<script setup>

import { ref } from 'vue'

const message = ref('Привет, Vue!')

</script>

<template>
  <div class="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<style scoped>
.app {
  text-align: center;
  padding: 2rem;
  font-family: system-ui, sans-serif;
}
</style>
