function getUserName(userId) {
    const user = database.findUser(userId);
    return user.name; // Ошибка, если user === null
}

function displayUserInfo(userId) {
    const name = getUserName(userId);
    document.getElementById('username').textContent = name;
}

function initPage() {
    const userId = getCurrentUserId();
    displayUserInfo(userId);
}

initPage();
