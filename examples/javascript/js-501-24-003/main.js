// Проверка значений переменных
document.querySelector('.header').style.color = 'red';

// Вызов функций
app.getUserData(123);

// Модификация состояния приложения
window.appState.user.loggedIn = false;

// Тестирование новых функций
function testHelper(value) {
    return value * 2;
}
testHelper(21); // 42
