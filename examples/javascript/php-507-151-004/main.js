const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    try {
        const response = await fetch('/submit.php', {
            method: 'POST',
            body: formData
        });
        const result = await response.text();
        alert(result);
    } catch (err) {
        console.error('Ошибка:', err);
    }
});
