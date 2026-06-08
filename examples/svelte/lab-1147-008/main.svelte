<script>
  import { onMount } from 'svelte'

  let notes = $state([])
  let error = $state('')
  let loading = $state(true)

  onMount(async () => {
    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      notes = await res.json()
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  })
</script>

<section>
  <h2>Записи с сервера</h2>
  {#if loading}
    <p>Загрузка…</p>
  {:else if error}
    <p>Ошибка: {error}</p>
  {:else}
    <ul>
      {#each notes as n (n.id)}
        <li>{n.title}</li>
      {/each}
    </ul>
  {/if}
</section>
