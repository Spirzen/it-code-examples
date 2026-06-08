from telegram import Bot

import asyncio

async def send_telegram_alert(token: str, chat_id: int, message: str):
    bot = Bot(token=token)
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=message,
            parse_mode='HTML',  # поддержка базовой HTML-разметки
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Ошибка отправки в Telegram: {e}")
        raise
