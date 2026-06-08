<script setup>

import { ref } from 'vue'

const email = ref('')
const isValid = ref(true)

const validate = () => {
  isValid.value = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
}
</script>

<template>
  <input v-model="email" @blur="validate" :class="{ error: !isValid }" />
  <p v-if="!isValid">Неверный email</p>
</template>
