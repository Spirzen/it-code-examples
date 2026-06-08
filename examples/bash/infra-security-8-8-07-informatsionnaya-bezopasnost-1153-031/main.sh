# Установка git-secrets
git secrets --install
git secrets --register-aws

# Добавление пользовательских паттернов
git secrets --add 'password\s*=\s*["\x27][^"\x27]+["\x27]'
git secrets --add 'api[_-]?key\s*=\s*["\x27][^"\x27]+["\x27]'
git secrets --add '-----BEGIN [A-Z ]+ PRIVATE KEY-----'
git secrets --add 'sk_live_[a-zA-Z0-9]{24,}'

# Сканирование репозитория
git secrets --scan

# Сканирование истории
git secrets --scan-history
