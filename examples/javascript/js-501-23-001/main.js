const list = document.getElementById('todo-list');
let nextId = 2;

document.getElementById('add').addEventListener('click', () => {
  const li = document.createElement('li');
  li.dataset.id = String(nextId++);
  li.innerHTML = `Задача ${li.dataset.id} <button type="button" data-action="delete">×</button>`;
  list.appendChild(li);
});

list.addEventListener('click', (event) => {
  const deleteBtn = event.target.closest('[data-action="delete"]');
  if (!deleteBtn || !list.contains(deleteBtn)) return;
  deleteBtn.closest('li')?.remove();
});
