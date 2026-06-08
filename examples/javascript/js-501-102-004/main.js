const formContainer = document.getElementById('form-area');
const newForm = document.createElement('form');
newForm.id = 'dynamicForm';
newForm.action = '/submit';
newForm.method = 'POST';

const label = document.createElement('label');
label.htmlFor = 'emailInput';
label.innerText = 'Email:';

const input = document.createElement('input');
input.type = 'email';
input.id = 'emailInput';
input.name = 'user_email';
input.required = true;

newForm.append(label, input);
formContainer.appendChild(newForm);
