try {
    decodeURIComponent("%"); // Некорректная последовательность
} catch (error) {
    console.log(error.name); // "URIError"
}

// Создание своей ошибки URI
function safeDecode(uriComponent) {
    try {
        return decodeURIComponent(uriComponent);
    } catch (error) {
        if (error instanceof URIError) {
            throw new URIError(`Некорректный URI-компонент: ${uriComponent}`);
        }
        throw error;
    }
}

try {
    safeDecode("%E0%A4%A");
} catch (error) {
    console.log(error.message); // "Некорректный URI-компонент: %E0%A4%A"
}
