const express = require('express');
const { cacheGet } = require('./cache');

const app = express();

// Эмуляция тяжёлого запроса к БД
async function fetchUserProfile(userId) {
  // Имитируем задержку
  await new Promise(r => setTimeout(r, 200));
  return { id: userId, name: `User ${userId}`, lastLogin: new Date().toISOString() };
}

app.get('/api/user/:id', async (req, res) => {
  const userId = req.params.id;
  const key = `cache:user:${userId}`;

  try {
    const profile = await cacheGet(key, () => fetchUserProfile(userId), 600);
    res.json(profile);
  } catch (err) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
