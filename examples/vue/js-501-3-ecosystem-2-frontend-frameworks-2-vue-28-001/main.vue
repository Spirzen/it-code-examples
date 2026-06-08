<script setup>

import { ref, computed } from 'vue'
import UserProfile from './UserProfile.vue'

const name = ref('Тимур')
const greeting = computed(() => `Привет, ${name.value}!`)
</script>

<template>
  <div>
    <input v-model="name" />
    <p>{{ greeting }}</p>
    <UserProfile :name="name" />
  </div>
</template>
