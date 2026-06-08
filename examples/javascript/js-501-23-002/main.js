const list = document.getElementById('list');
const doneZone = document.getElementById('done-zone');

list.addEventListener('dragstart', (event) => {
  if (!event.target.matches('li[draggable]')) return;
  event.dataTransfer.setData('text/plain', event.target.dataset.id);
  event.dataTransfer.effectAllowed = 'move';
});

doneZone.addEventListener('dragover', (event) => {
  event.preventDefault();
  event.dataTransfer.dropEffect = 'move';
});

doneZone.addEventListener('drop', (event) => {
  event.preventDefault();
  const id = event.dataTransfer.getData('text/plain');
  const item = list.querySelector(`[data-id="${id}"]`);
  if (item) doneZone.appendChild(item);
});
