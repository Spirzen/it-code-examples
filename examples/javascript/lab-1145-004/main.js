const [postRes, commentsRes] = await Promise.all([
  fetch('https://jsonplaceholder.typicode.com/posts/1'),
  fetch('https://jsonplaceholder.typicode.com/posts/1/comments'),
]);

if (!postRes.ok || !commentsRes.ok) {
  throw new Error('Один из запросов завершился ошибкой');
}

const [post, comments] = await Promise.all([
  postRes.json
  commentsRes.json
]);

console.log(post.title, 'комментариев:', comments.length);
