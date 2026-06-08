<script setup>

import { ref } from 'vue'
import Counter from './components/Counter.vue'

const count = ref(0)

</script>

<template>
  <Counter
    :value="count"
    @increment="count++"
    @decrement="count--"
    @reset="count = 0"
  />
</template>
