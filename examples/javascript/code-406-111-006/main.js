// JavaScript в браузере — синхронные необработанные ошибки
window.addEventListener('error', (event) => {
    console.error('Глобальная ошибка:', event.error);
});

// Отклонённые Promise без .catch / await в try
window.addEventListener('unhandledrejection', (event) => {
    console.error('Необработанный rejection:', event.reason);
});
