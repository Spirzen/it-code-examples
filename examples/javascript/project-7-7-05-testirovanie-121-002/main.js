// Проверка статуса
pm.test("Status 201 Created", () => {
    pm.response.to.have.status(201);
});

// Проверка Content-Type
pm.test("Content-Type is application/json", () => {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});

// Парсинг ответа
const response = pm.response.json();

// Проверка обязательных полей
pm.test("Response has required fields", () => {
    pm.expect(response).to.have.property("id");
    pm.expect(response).to.have.property("title", "Изучить интеграционное тестирование");
    pm.expect(response).to.have.property("status", "pending");
    pm.expect(response).to.have.property("createdAt");
    pm.expect(response).to.have.property("updatedAt");
});

// Сохранение ID для последующих запросов
pm.globals.set("created_task_id", response.id);
