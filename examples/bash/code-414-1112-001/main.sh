# Поиск потенциально опасных файлов в проекте (Linux/macOS)
find . -type f \( \
    -name "*.env" -o \
    -name "*.key" -o \
    -name "*.pem" -o \
    -name "*secret*" -o \
    -name "*password*" -o \
    -name "id_*" -o \
    -name "*.token" -o \
    -name "wallet.dat" -o \
    -name "*.keyring" -o \
    -name "*.pypirc" -o \
    -name ".npmrc" -o \
    -name "*.p12" -o \
    -name "*.pfx" \
\) 2>/dev/null

# Проверка коммитов Git на наличие конфиденциальных данных
git log --all --full-history -- \
    "*password*" "*secret*" "*.key" ".env" ".pem"
