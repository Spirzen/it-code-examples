<script setup>

import { ref, computed } from 'vue'

const email = ref('')
const submitted = ref(false)

const emailError = computed(() => {
  if (!submitted.value) return ''
  if (!email.value.includes('@')) return 'Нужен символ @'
  return ''
})

const onSubmit = () => {
  submitted.value = true
  if (!emailError.value) alert(`Отправлено: ${email.value}`)
}

</script>

<template>
  <form @submit.prevent="onSubmit">
    <label>
      Email
      <input v-model="email" type="email" />
    </label>
    <p v-if="emailError" class="err">{{ emailError }}</p>
    <button type="submit">Отправить</button>
  </form>
</template>

<style scoped>
.err { color: #c00; font-size: 0.9rem; }
</style>
