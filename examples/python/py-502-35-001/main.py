#!/usr/bin/env python3
"""
Автоматическая архивация лог-файлов.

Скрипт просматривает указанный каталог, находит файлы старше заданного возраста,
сжимает их в tar.gz-архивы и перемещает в архивный каталог. Перед архивацией
проверяется свободное место. Все действия логируются в JSON-формате.

Требования:
- Python ≥ 3.8
- Не требует сторонних зависимостей.

Использование:
    python log_archiver.py \
        --source /var/log/app \
        --archive /var/log/archive \
        --days 30 \
        --min-free-space 1GB \
        --dry-run

Переменные окружения (альтернатива CLI):
    LOG_ARCHIVER_SOURCE      — каталог с логами
    LOG_ARCHIVER_ARCHIVE     — каталог архивов
    LOG_ARCHIVER_DAYS        — порог возраста (в днях)
    LOG_ARCHIVER_MIN_FREE    — минимальный объём свободного места (например, "2.5GB")
    LOG_ARCHIVER_DRY_RUN     — "1" для тестового прогона без изменений
    TELEGRAM_BOT_TOKEN       — токен бота (опционально, для алертов)
    TELEGRAM_CHAT_ID         — ID чата (опционально)
"""

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
import time

from datetime import datetime, timedelta
from pathlib import Path


# === Настройка логгера ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("/var/log/log_archiver.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def parse_size(size_str: str) -> int:
    """Преобразует строку вида '1.5GB' в байты."""
    size_str = size_str.upper().strip()
    multipliers = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4}
    for unit, mult in multipliers.items():
        if size_str.endswith(unit):
            try:
                value = float(size_str[: -len(unit)].strip())
                return int(value * mult)
            except ValueError:
                pass
    raise ValueError(f"Некорректный формат размера: {size_str}")


def get_free_space(path: Path) -> int:
    """Возвращает свободное место на устройстве в байтах."""
    stat = os.statvfs(path)
    return stat.f_bavail * stat.f_frsize


def archive_file(file_path: Path, archive_dir: Path, dry_run: bool = False) -> bool:
    """Архивирует один файл в tar.gz и удаляет оригинал при успехе."""
    try:
        archive_name = f"{file_path.stem}_{file_path.stat().st_mtime:.0f}.tar.gz"
        archive_path = archive_dir / archive_name

        if dry_run:
            logger.info(f"[DRY-RUN] Будет создан архив: {archive_path}")
            return True

        # Создаём архив с сохранением прав и времён
        cmd = [
            "tar",
            "-czf",
            str(archive_path),
            "-C",
            str(file_path.parent),
            file_path.name,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logger.debug(f"tar stdout: {result.stdout}")
        logger.debug(f"tar stderr: {result.stderr}")

        # Удаляем оригинал только после успешного архивирования
        file_path.unlink()
        logger.info(f"Архивирован и удалён: {file_path} → {archive_path}")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка tar для {file_path}: {e.stderr}")
        return False
    except Exception as e:
        logger.exception(f"Необработанная ошибка при архивации {file_path}: {e}")
        return False


def send_telegram_alert(message: str):
    """Отправляет уведомление в Telegram (если настроены токен и chat_id)."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        return

    try:
        import requests  # lazy import — только при необходимости
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": f"[LogArchiver] {message}",
            "parse_mode": "Markdown",
        }
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        logger.warning(f"Не удалось отправить Telegram-алерт: {e}")


def main():
    parser = argparse.ArgumentParser(description="Автоархивация логов")
    parser.add_argument("--source", required=False, help="Каталог с логами")
    parser.add_argument("--archive", required=False, help="Каталог для архивов")
    parser.add_argument("--days", type=int, default=30, help="Возраст файлов в днях")
    parser.add_argument(
        "--min-free-space", default="1GB", help="Минимум свободного места (напр., 2.5GB)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Тестовый прогон")

    args = parser.parse_args()

    # Приоритет: CLI > ENV > default (но source/archive обязательны)
    source_dir = Path(args.source or os.getenv("LOG_ARCHIVER_SOURCE"))
    archive_dir = Path(args.archive or os.getenv("LOG_ARCHIVER_ARCHIVE"))
    days = args.days or int(os.getenv("LOG_ARCHIVER_DAYS", 30))
    min_free = args.min_free_space or os.getenv("LOG_ARCHIVER_MIN_FREE", "1GB")
    dry_run = args.dry_run or os.getenv("LOG_ARCHIVER_DRY_RUN") == "1"

    if not source_dir or not archive_dir:
        logger.error("Не указаны --source и --archive (или переменные окружения)")
        sys.exit(1)

    try:
        min_bytes = parse_size(min_free)
        cutoff_time = time.time() - days * 86400  # 86400 = секунд в дне
        archive_dir.mkdir(parents=True, exist_ok=True)

        # Проверка свободного места
        free_bytes = get_free_space(archive_dir)
        if free_bytes < min_bytes:
            msg = f"Недостаточно места в {archive_dir}: {free_bytes / 1e9:.2f} GB < {min_free}"
            logger.error(msg)
            send_telegram_alert(msg)
            sys.exit(1)

        # Сбор подходящих файлов
        candidates = [
            f
            for f in source_dir.rglob("*")
            if f.is_file() and f.stat().st_mtime < cutoff_time
        ]

        logger.info(f"Найдено {len(candidates)} файлов старше {days} дней в {source_dir}")

        success_count = 0
        for file in candidates:
            if archive_file(file, archive_dir, dry_run):
                success_count += 1

        summary = (
            f"Архивация завершена: {success_count}/{len(candidates)} файлов обработано."
        )
        logger.info(summary)
        if not dry_run and len(candidates) > 0:
            send_telegram_alert(summary)

    except Exception as e:
        error_msg = f"Критическая ошибка: {e}"
        logger.exception(error_msg)
        send_telegram_alert(error_msg)
        sys.exit(1)


if __name__ == "__main__":
    main()
