// Сервис уведомлений: важно, ЧТО вызвали, а не что вернулось
async function onUserRegistered(user, notifications) {
  await notifications.send({
    to: user.email,
    subject: 'Добро пожаловать',
    body: `Здравствуйте, ${user.name}`,
  });
}

// --- тест (sinon) ---
const sinon = require('sinon');

test('после регистрации отправляется одно приветственное письмо', async () => {
  const mailer = { send: sinon.stub().resolves() };
  const user = { name: 'Аня', email: 'anya@example.com' };

  await onUserRegistered(user, mailer);

  sinon.assert.calledOnce(mailer.send);
  sinon.assert.calledWith(mailer.send, {
    to: 'anya@example.com',
    subject: 'Добро пожаловать',
    body: 'Здравствуйте, Аня',
  });
});
