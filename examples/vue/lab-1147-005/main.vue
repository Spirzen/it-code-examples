<script setup>

import { ref } from 'vue'

const newTask = ref('')
const tasks = ref([
  { id: 1, text: 'Изучить ref и v-model', done: false },
])

let nextId = 2

const addTask = () => {
  const text = newTask.value.trim()
  if (!text) return
  tasks.value.push({ id: nextId++, text, done: false })
  newTask.value = ''
}

const removeTask = (id) => {
  tasks.value = tasks.value.filter((t) => t.id !== id)
}

</script>

<template>
  <section class="todo">
    <h2>Список задач</h2>
    <form @submit.prevent="addTask">
      <input v-model="newTask" placeholder="Новая задача" />
      <button type="submit">Добавить</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <label>
          <input type="checkbox" v-model="task.done" />
          <span :class="{ done: task.done }">{{ task.text }}</span>
        </label>
        <button type="button" @click="removeTask(task.id)">×</button>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.done { text-decoration: line-through; color: #888; }
.todo ul { list-style: none; padding: 0; }
.todo li { display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0; }
</style>
