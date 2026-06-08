const Redis = require('ioredis');

// Подключение с учётом ACL
const redis = new Redis({
  host: '127.0.0.1',
  port: 6379,
  username: 'appuser',
  password: 'Str0ngP@ss',
  // Отказоустойчивость: автоматическое переподключение
  retryStrategy(times) {
    const delay = Math.min(times * 50, 2000);
    return delay;
  },
  // Таймауты (защита от зависаний)
  connectTimeout: 3000,
  commandTimeout: 2000,
});

// Функция-обёртка для кэширования
async function cacheGet(key, fetchFn, ttl = 300) {
  try {
    // Шаг 1: Попытка чтения из кэша
    const cached = await redis.get(key);
    if (cached) {
      console.log(`[CACHE HIT] ${key}`);
      return JSON.parse(cached);
    }

    // Шаг 2: Вычисление (запрос к БД, внешнему API и т.п.)
    console.log(`[CACHE MISS] ${key}`);
    const data = await fetchFn();

    // Шаг 3: Сохранение в кэш (только если данные получены)
    if (data !== undefined && data !== null) {
      await redis.set(key, JSON.stringify(data), 'EX', ttl);
    }

    return data;
  } catch (err) {
    // При ошибке Redis — прозрачно работаем без кэша
    console.warn(`[CACHE ERROR] ${err.message}`);
    return fetchFn();
  }
}

module.exports = { redis, cacheGet };
