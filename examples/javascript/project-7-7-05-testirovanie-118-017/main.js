
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },   // Разгон до 10 пользователей за 30 секунд
    { duration: '1m', target: 10 },    // Удержание нагрузки 1 минуту
    { duration: '30s', target: 0 },    // Сброс нагрузки за 30 секунд
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% запросов должны быть быстрее 500 мс
    http_req_failed: ['rate<0.01'],   // Уровень ошибок не более 1%
  },
};

export default function () {
  const res = http.get('https://example.com/api/health');
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1); // Пауза между запросами
}
