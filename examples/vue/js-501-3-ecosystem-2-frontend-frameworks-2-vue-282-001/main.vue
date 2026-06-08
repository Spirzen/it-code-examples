<script setup>

import { ref } from 'vue'

const count = ref(0)
const name = ref('')

const increment = () => { count.value++ }
const decrement = () => { count.value-- }
const reset = () => { count.value = 0 }
</script>

<template>
  <div class="app">
    <h1>Моя первая программа на Vue.js</h1>

    <section class="greeting">
      <input v-model="name" type="text" placeholder="Введите ваше имя" />
      <h2 v-if="name">Привет, {{ name }}!</h2>
    </section>

    <section class="counter">
      <h2>Счётчик: {{ count }}</h2>
      <div class="buttons">
        <button type="button" @click="decrement">−</button>
        <button type="button" @click="reset">Сброс</button>
        <button type="button" @click="increment">+</button>
      </div>
    </section>
  </div>
</template>

<style scoped>
.app { text-align: center; padding: 2rem; font-family: system-ui, sans-serif; }
.greeting { margin: 1.5rem 0; padding: 1.25rem; background: #f0f0f0; border-radius: 10px; }
.counter { margin: 1.5rem 0; padding: 1.25rem; background: #e8f4f8; border-radius: 10px; }
input { padding: 0.5rem 0.75rem; font-size: 1rem; border: 2px solid #ddd; border-radius: 6px; }
button {
  margin: 0 4px; padding: 0.5rem 1rem; font-size: 1rem;
  background: #42b883; color: #fff; border: none; border-radius: 6px; cursor: pointer;
}
button:hover { background: #3aa876; }
</style>
