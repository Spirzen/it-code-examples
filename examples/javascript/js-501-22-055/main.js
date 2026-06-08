// Promise.all - ожидание всех промисов
Promise.all([
    fetch("/api/users"),
    fetch("/api/posts"),
    fetch("/api/comments")
])
.then(responses => Promise.all(responses.map(r => r.json())))
.then(([users, posts, comments]) => {
    console.log("data загружены:", { users, posts, comments });
});

// Promise.race - возвращает первый завершённый промис
Promise.race([
    fetch("/api/data"),
    new Promise((_, reject) => 
        setTimeout(() => reject(new Error("Таймаут")), 5000)
    )
])
.then(data => console.log("Данные получены"))
.catch(error => console.error("Ошибка:", error));

// Promise.allSettled - ожидает все промисы независимо от результата
Promise.allSettled([
    Promise.resolve(1),
    Promise.reject(new Error("Ошибка")),
    Promise.resolve(3)
])
.then(results => {
    results.forEach((result, index) => {
        if (result.status === "fulfilled") {
            console.log(`Промис ${index} выполнен:`, result.value);
        } else {
            console.log(`Промис ${index} отклонён:`, result.reason);
        }
    });
});
