<script>
  let newTask = $state('')
  let tasks = $state([
    { id: 1, text: 'Изучить $state и {#each}', done: false },
  ])
  let nextId = 2

  function addTask() {
    const text = newTask.trim()
    if (!text) return
    tasks = [..tasks, { id: nextId++, text, done: false }]
    newTask = ''
  }

  function removeTask(id) {
    tasks = tasks.filter((t) => t.id !== id)
  }
</script>

<section class="todo">
  <h2>Список задач</h2>
  <form onsubmit={(e) => { e.preventDefault(); addTask() }}>
    <input bind:value={newTask} placeholder="Новая задача" />
    <button type="submit">Добавить</button>
  </form>
  <ul>
    {#each tasks as task (task.id)}
      <li>
        <label>
          <input type="checkbox" bind:checked={task.done} />
          <span class:done={task.done}>{task.text}</span>
        </label>
        <button type="button" onclick={() => removeTask(task.id)}>×</button>
      </li>
    {/each}
  </ul>
</section>

<style>
  .done { text-decoration: line-through; color: #888; }
  .todo ul { list-style: none; padding: 0; }
  .todo li { display: flex; justify-content: space-between; margin: 0.5rem 0; }
</style>
