function levelThree() {
    const data = null;
    return data.value; // Ошибка здесь
}

function levelTwo() {
    return levelThree();
}

function levelOne() {
    return levelTwo();
}

function start() {
    return levelOne();
}

start();
