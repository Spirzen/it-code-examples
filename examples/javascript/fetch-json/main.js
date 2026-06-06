export async function loadPosts(limit = 3) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts?_limit=${limit}`);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`);
  }
  return res.json();
}

loadPosts()
  .then((posts) => console.table(posts.map((p) => ({id: p.id, title: p.title}))))
  .catch(console.error);
