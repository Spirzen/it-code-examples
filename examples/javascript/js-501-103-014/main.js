// Этот код работает и в браузере, и в Node.js

function countWords(text) {
    if (typeof text !== 'string') {
        throw new Error('Входные данные должны быть строкой');
    }

    const words = text.trim().split(/\s+/);
    const filteredWords = words.filter(word => word.length > 0);
    
    return {
        total: filteredWords.length,
        unique: new Set(filteredWords).size,
        list: filteredWords
    };
}

// Режим выполнения
if (typeof window === 'undefined') {
    // Мы находимся в Node.js
    const textInput = "JavaScript - это язык программирования. JavaScript очень популярен.";
    const result = countWords(textInput);
    
    console.log('Текст:', textInput);
    console.log('Всего слов:', result.total);
    console.log('Уникальных слов:', result.unique);
    console.log('Список слов:', result.list);
} else {
    // Мы находимся в браузере
    document.getElementById('result').innerText = JSON.stringify(countWords(document.getElementById('input').value));
}
