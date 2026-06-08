pm.test("Status 204 No Content", () => {
    pm.response.to.have.status(204);
});

// Дополнительно: попытка получить удалённую задачу → должен быть 404
// (Здесь можно использовать pm.sendRequest для цепочки внутри одного Tests)
pm.sendRequest({
    url: `${pm.environment.get('base_url')}/Задачи/${pm.globals.get('created_task_id')}`,
    method: 'GET'
}, (err, res) => {
    pm.test("GET after DELETE returns 404", () => {
        pm.expect(res.code).to.eql(404);
    });
});
