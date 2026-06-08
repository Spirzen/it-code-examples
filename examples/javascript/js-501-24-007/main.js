async function loadData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return processData(data);
    } catch (error) {
        console.error('Ошибка загрузки данных:', error);
        throw error;
    }
}

function processData(data) {
    return data.items.map(item => item.value);
}
