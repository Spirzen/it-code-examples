
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 100,           // виртуальных пользователей
  duration: '30s',    // продолжительность теста
  thresholds: {       // SLO-ограничения
    'http_req_duration{staticAsset: true}': ['p(95) < 100'],
    'http_req_failed': ['rate < 0.01'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://example.com';

export default function () {
  // Запрос статического ресурса
  const res1 = http.get(`${BASE_URL}/styles/main.css`, {
    tags: { staticAsset: true },
  });
  check(res1, {
    'CSS loaded': (r) => r.status === 200,
  });

  // Имитация задержки чтения
  sleep(1);

  // Авторизация
  const res2 = http.post(`${BASE_URL}/login`, {
    user: 'test',
    password: 'secret',
  });
  const token = res2.json('token');
  check(res2, {
    'login succeeded': (r) => r.status === 200 && token,
  });

  // Защищённый запрос
  http.get(`${BASE_URL}/profile`, {
    headers: { Authorization: `Bearer ${token}` },
  });

  sleep(2);
}
