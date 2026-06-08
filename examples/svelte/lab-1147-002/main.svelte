<script>
  let message = $state('Привет, Svelte!')
</script>

<main>
  <h1>{message}</h1>
</main>

<style>
  main {
    text-align: center;
    padding: 2rem;
    font-family: system-ui, sans-serif;
  }
</style>
