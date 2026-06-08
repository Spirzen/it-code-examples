const request = require('supertest');
const app = require('../src/app'); // ваше Express-приложение

describe('Задачи API', () => {
  it('creates a task with valid Данные', async () => {
    const res = await request(app)
      .post('/api/Задачи')
      .send({
        title: 'Тестирование через Supertest',
        description: 'Без запуска сервера'
      })
      .expect(201);

    expect(res.body).toMatchObject({
      id: expect.any(Number),
      title: 'Тестирование через Supertest',
      status: 'pending'
    });
  });
});
