#!/usr/bin/env python3
"""
Health-check монитор с Telegram-оповещением.

Проверяет доступность списка сервисов по HTTP и ICMP. При N последовательных
провалах отправляет алерт в Telegram. Поддерживает кастомные проверки (например,
наличие ключевой фразы в теле ответа).

Требования:
    pip install requests ping3

Конфигурация — через YAML-файл (см. пример ниже) или переменные окружения.

Пример config.yaml:
    services:
      - name: "API Gateway"
        url: "https://api.example.com/health"
        timeout: 5
        expected_status: 200
        expected_text: "OK"
        failure_threshold: 3

      - name: "Database Host"
        host: "db.internal"
        type: "icmp"
        failure_threshold: 2

    telegram:
        bot_token: "${TELEGRAM_BOT_TOKEN}"  # подстановка из env
        chat_id: "${TELEGRAM_CHAT_ID}"
"""

import argparse
import json
import logging
import os
import sys
import time
import yaml

from pathlib import Path

import requests

from ping3 import ping


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


class HealthMonitor:
    def __init__(self, config_path: str):
        with open(config_path) as f:
            raw_config = yaml.safe_load(f)

        # Подстановка переменных окружения вида ${VAR}
        config_str = json.dumps(raw_config)
        for key, value in os.environ.items():
            config_str = config_str.replace(f"${{{key}}}", value)
        self.config = json.loads(config_str)

        self.state = {}  # имя сервиса → счётчик провалов

    def check_http(self, service: dict) -> bool:
        try:
            resp = requests.get(
                service["url"],
                timeout=service.get("timeout", 10),
                headers={"User-Agent": "HealthMonitor/1.0"},
            )
            if resp.status_code != service.get("expected_status", 200):
                logger.warning(f"{service['name']}: статус {resp.status_code}")
                return False
            if (text := service.get("expected_text")) and text not in resp.text:
                logger.warning(f"{service['name']}: не найден текст '{text}'")
                return False
            return True
        except Exception as e:
            logger.error(f"{service['name']}: HTTP ошибка — {e}")
            return False

    def check_icmp(self, service: dict) -> bool:
        try:
            delay = ping(service["host"], timeout=service.get("timeout", 2))
            return delay is not None
        except Exception as e:
            logger.error(f"{service['name']}: ICMP ошибка — {e}")
            return False

    def check_service(self, service: dict) -> bool:
        check_type = service.get("type", "http")
        if check_type == "http":
            return self.check_http(service)
        elif check_type == "icmp":
            return self.check_icmp(service)
        else:
            logger.error(f"Неизвестный тип проверки: {check_type}")
            return False

    def run_once(self):
        for svc in self.config["services"]:
            name = svc["name"]
            is_ok = self.check_service(svc)

            # Инициализация состояния
            if name not in self.state:
                self.state[name] = 0

            if is_ok:
                if self.state[name] > 0:
                    logger.info(f"{name}: восстановлен после {self.state[name]} сбоев")
                    self._send_alert(f"✅ {name} восстановлен")
                self.state[name] = 0
            else:
                self.state[name] += 1
                threshold = svc.get("failure_threshold", 3)
                if self.state[name] >= threshold:
                    self._send_alert(f"❌ {name} недоступен ({self.state[name]} сбоев подряд)")

    def _send_alert(self, message: str):
        tg = self.config.get("telegram", {})
        token = tg.get("bot_token")
        chat_id = tg.get("chat_id")
        if not token or not chat_id:
            return

        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {"chat_id": chat_id, "text": f"[HealthMonitor] {message}"}
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            logger.warning(f"Ошибка отправки Telegram: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml", help="Путь к конфигу")
    parser.add_argument("--interval", type=int, default=60, help="Интервал проверки (сек)")
    args = parser.parse_args()

    try:
        monitor = HealthMonitor(args.config)
        logger.info(f"Запущен мониторинг с интервалом {args.interval} сек")
        while True:
            monitor.run_once()
            time.sleep(args.interval)
    except KeyboardInterrupt:
        logger.info("Остановлен пользователем")
    except Exception as e:
        logger.exception(f"Критическая ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
