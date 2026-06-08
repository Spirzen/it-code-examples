const message = document.getElementById('message');
const button = document.getElementById('btn');

let clicks = 0;

button.addEventListener('click', () => {
  clicks += 1;
  message.textContent =
    clicks === 1
      ? 'Кнопка сработала — JavaScript на Pages работает.'
      : `Нажатий: ${clicks}. Можно менять текст и стили, пушить снова — сайт обновится.`;
});
