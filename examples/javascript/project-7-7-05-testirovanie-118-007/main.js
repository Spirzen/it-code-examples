const request = require('supertest');
const app = require('../src/app');

describe('POST /api/users', () => {
  it('должен создавать нового пользователя', async () => {
    const newUser = { name: 'Ivan', email: 'ivan@example.com' };

    const response = await request(app)
      .post('/api/users')
      .send(newUser)
      .set('Content-Type', 'application/json')
      .expect(201)
      .expect('Content-Type', /json/)
      .then(res => {
        expect(res.body.name).toBe(newUser.name);
        expect(res.body.email).toBe(newUser.email);
        expect(res.body.id).toBeDefined();
      });
  });
});
