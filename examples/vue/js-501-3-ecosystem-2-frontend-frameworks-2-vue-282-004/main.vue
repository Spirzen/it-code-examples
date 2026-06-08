<script>
export default {
  data() {
    return { count: 0, name: '' }
  },
  methods: {
    increment() { this.count++ },
    decrement() { this.count-- },
    reset() { this.count = 0 },
  },
}
</script>

<template>
  <h2>Счётчик: {{ count }}</h2>
  <input v-model="name" />
  <button type="button" @click="increment">+</button>
</template>
