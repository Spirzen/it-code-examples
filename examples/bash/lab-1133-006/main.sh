# GET
curl -s "URL"

# GET + только код
curl -s -o /dev/null -w "%{http_code}\n" "URL"

# POST JSON
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"key":"value"}' "URL"

# Заголовки + тело
curl -s -i "URL"

# Токен
curl -s -H "Authorization: Bearer TOKEN" "URL"
