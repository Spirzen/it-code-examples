<script>
  let count = $state(0)
  let name = $state('')

  function increment() { count += 1 }
  function decrement() { count -= 1 }
  function reset() { count = 0 }
</script>

<main>
  <h1>Моя первая программа на Svelte</h1>

  <section class="greeting">
    <input bind:value={name} type="text" placeholder="Введите имя" />
    {#if name}
      <h2>Привет, {name}!</h2>
    {/if}
  </section>

  <section class="counter">
    <h2>Счётчик: {count}</h2>
    <button type="button" onclick={decrement}>−</button>
    <button type="button" onclick={reset}>Сброс</button>
    <button type="button" onclick={increment}>+</button>
  </section>
</main>

<style>
  main { text-align: center; padding: 2rem; }
  .greeting, .counter { margin: 1.5rem 0; padding: 1rem; border-radius: 8px; }
  .greeting { background: #f0f0f0; }
  .counter { background: #fff3e0; }
  button {
    margin: 0 4px;
    padding: 0.5rem 1rem;
    background: #ff3e00;
    color: #fff;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
</style>
