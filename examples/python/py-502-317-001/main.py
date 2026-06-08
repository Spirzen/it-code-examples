
import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я учебный бот.\n"
        "Команды: /start, /help, /echo <текст>",
    )

@bot.message_handler(commands=["echo"])
def echo(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "Напишите: /echo ваш текст")
        return
    bot.reply_to(message, parts[1])

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.reply_to(message, "Не понял. Попробуйте /help")

if __name__ == "__main__":
    bot.infinity_polling()
