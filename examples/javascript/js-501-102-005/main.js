const addBtn = document.querySelector('.add-item-btn');
const list = document.querySelector('.task-list');

addBtn.addEventListener('click', function() {
    const taskText = prompt('Введите название задачи:');
    
    if (!taskText) return;

    const li = document.createElement('li');
    li.className = 'task-item pending';
    li.innerText = taskText;

    const deleteBtn = document.createElement('button');
    deleteBtn.innerText = 'Удалить';
    deleteBtn.className = 'delete-btn';
    
    deleteBtn.addEventListener('click', function() {
        li.remove();
    });

    li.appendChild(deleteBtn);
    list.appendChild(li);
});
