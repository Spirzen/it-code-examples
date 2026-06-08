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
    <h1>Моя первая программа на Vue</h1>

    <section class="greeting">
      <input v-model="name" type="text" placeholder="Введите имя" />
      <h2 v-if="name">Привет, {{ name }}!</h2>
    </section>

    <section class="counter">
      <h2>Счётчик: {{ count }}</h2>
      <button type="button" @click="decrement">−</button>
      <button type="button" @click="reset">Сброс</button>
      <button type="button" @click="increment">+</button>
    </section>
  </div>
</template>

<style scoped>
.app { text-align: center; padding: 2rem; }
.greeting, .counter { margin: 1.5rem 0; padding: 1rem; border-radius: 8px; }
.greeting { background: #f0f0f0; }
.counter { background: #e8f4f8; }
button {
  margin: 0 4px;
  padding: 0.5rem 1rem;
  background: #42b883;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
button:hover { background: #3aa876; }
</style>
