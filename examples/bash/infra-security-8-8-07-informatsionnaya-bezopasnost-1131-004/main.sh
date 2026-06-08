#!/bin/bash

echo "=== Аудит безопасности конфигурации ==="

# Проверка версии OpenSSL
OPENSSL_VERSION=$(openssl version | awk '{print $2}')
echo "OpenSSL версия: $OPENSSL_VERSION"
if [[ "$OPENSSL_VERSION" < "1.1.1" ]]; then
    echo "[КРИТИЧНО] Требуется обновление OpenSSL"
fi

# Проверка настроек SSH
echo "=== Проверка SSH конфигурации ==="
if grep -q "PermitRootLogin yes" /etc/ssh/sshd_config; then
    echo "[ВНИМАНИЕ] Разрешен вход под root"
fi

if ! grep -q "PasswordAuthentication no" /etc/ssh/sshd_config; then
    echo "[ВНИМАНИЕ] Рекомендуется использовать ключи вместо паролей"
fi

# Проверка прав доступа к критичным файлам
echo "=== Проверка прав доступа ==="
CRITICAL_FILES=("/etc/shadow" "/etc/passwd" "/etc/sudoers")
for file in "${CRITICAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        PERMS=$(stat -c %a "$file")
        if [ "$PERMS" != "600" ] && [ "$file" = "/etc/shadow" ]; then
            echo "[ВНИМАНИЕ] Некорректные права для $file: $PERMS"
        fi
    fi
done

# Проверка установленных обновлений безопасности
echo "=== Проверка обновлений ==="
SECURITY_UPDATES=$(apt list --upgradable 2>/dev/null | grep -i security | wc -l)
if [ "$SECURITY_UPDATES" -gt 0 ]; then
    echo "[ВНИМАНИЕ] Доступно $SECURITY_UPDATES обновлений безопасности"
fi

echo "=== Аудит завершен ==="
