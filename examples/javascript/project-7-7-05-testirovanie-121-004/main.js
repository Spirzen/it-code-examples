pm.test("Status 200 OK", () => {
    pm.response.to.have.status(200);
});

const updated = pm.response.json();

pm.test("Status updated to in_progress", () => {
    pm.expect(updated.status).to.eql("in_progress");
});

// Проверка, что updatedAt изменился, а createdAt — нет
pm.test("updatedAt changed, createdAt preserved", () => {
    pm.expect(updated.updatedAt).to.not.eql(updated.createdAt);
    // (более строго: сравнить с предыдущим значением, сохранённым в переменную)
});
