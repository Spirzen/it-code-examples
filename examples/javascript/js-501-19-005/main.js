// --- Non-Strict Mode (по умолчанию в старых версиях или без 'use strict') ---
console.log('=== Non-Strict Mode ===');
function checkGlobal() {
    console.log(this); 
    // В браузере: Window {...}
    // В Node.js: global {...}
}
checkGlobal();

// --- Strict Mode ('use strict') ---
'use strict';

function checkGlobalStrict() {
    console.log(this); 
    // Результат: undefined (ошибка при попытке доступа к свойствам этого объекта)
}
checkGlobalStrict();

// Попытка использовать this в strict mode как объект вызовет ошибку:
try {
    const val = this.someProp; 
} catch (e) {
    console.error("Ошибка:", e.message); // TypeError: Cannot read properties of undefined
}
