const form = document.getElementById('signup');
const login = document.getElementById('login');
const loginError = document.getElementById('login-error');

login.addEventListener('input', () => {
  login.setCustomValidity('');
  loginError.hidden = true;
});

form.addEventListener('submit', (event) => {
  if (!form.checkValidity()) {
    event.preventDefault();
    if (!login.validity.valid) {
      loginError.textContent = login.validationMessage;
      loginError.hidden = false;
      login.focus();
    }
    return;
  }
  // отправка fetch или form.submit() на сервер
});
