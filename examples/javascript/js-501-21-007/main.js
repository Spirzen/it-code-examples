fetch('/api/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: 'Мой пост',
    content: 'Привет, мир!'
  })
})
.then(response => response.json())
.then(newPost => {
  console.log('Создано:', newPost);
});
