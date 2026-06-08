const form = document.getElementById('contact-form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    try {
        const response = await fetch('/submit.php', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            alert('Форма отправлена!');
            form.reset();
        } else {
            alert('Ошибка: ' + response.status);
        }
    } catch (err) {
        console.error('Сбой сети:', err);
    }
});
