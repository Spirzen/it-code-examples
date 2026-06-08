# Создание репозитория через API
curl -X POST https://gitverse.ru/api/v1/repos \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "visibility": "private",
    "description": "Мой проект разработки"
  }'

# Получение списка репозиториев
curl -X GET https://gitverse.ru/api/v1/repos \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -o repos.json
