<script setup>
defineProps({
  value: { type: Number, required: true },
})
const emit = defineEmits(['increment', 'decrement', 'reset'])
</script>

<template>
  <section class="counter">
    <h2>Счётчик: {{ value }}</h2>
    <button type="button" @click="emit('decrement')">−</button>
    <button type="button" @click="emit('reset')">Сброс</button>
    <button type="button" @click="emit('increment')">+</button>
  </section>
</template>
