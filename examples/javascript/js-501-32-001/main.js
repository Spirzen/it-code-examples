const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const result = document.getElementById('result');
const error = document.getElementById('error');
const buttons = document.querySelectorAll('.buttons button');
const equals = document.querySelector('.equals');

let operation = null;

buttons.forEach(button => {
  button.addEventListener('click', () => {
    operation = button.textContent;
  });
});

equals.addEventListener('click', () => {
  const a = Number(num1.value);
  const b = Number(num2.value);
  
  if (!operation) {
    error.textContent = 'Выберите операцию';
    return;
  }

  let res;
  switch(operation) {
    case '+': res = a + b; break;
    case '-': res = a - b; break;
    case '×': res = a * b; break;
    case '÷': res = b !== 0 ? a / b : 'Ошибка';
  }

  result.textContent = res === 'Ошибка' ? res : res.toFixed(2);
  error.textContent = res === 'Ошибка' ? 'Деление на ноль' : '';
});

