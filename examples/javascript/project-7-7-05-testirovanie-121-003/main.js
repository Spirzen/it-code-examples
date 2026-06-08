pm.test("Status 200 OK", () => {
    pm.response.to.have.status(200);
});

const task = pm.response.json();

pm.test("Task Данные matches created", () => {
    pm.expect(task.title).to.eql("Изучить интеграционное тестирование");
    pm.expect(task.status).to.eql("pending");
});

// Проверка, что createdAt и updatedAt — валидные ISO-строки
pm.test("Timestamps are valid ISO strings", () => {
    pm.expect(new Date(task.createdAt).toString()).to.not.equal("Invalid Date");
    pm.expect(new Date(task.updatedAt).toString()).to.not.equal("Invalid Date");
});
