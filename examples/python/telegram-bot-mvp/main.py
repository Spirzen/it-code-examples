import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

USER_TASKS: dict[int, list[str]] = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я учебный бот. Команды: /help, /task, /list")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("/task ТЕКСТ - добавить задачу\n/list - показать задачи")


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    text = " ".join(context.args).strip()
    if not text:
        await update.message.reply_text("Передайте текст: /task Купить молоко")
        return
    USER_TASKS.setdefault(user_id, []).append(text)
    await update.message.reply_text("Задача добавлена.")


async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    tasks = USER_TASKS.get(user_id, [])
    if not tasks:
        await update.message.reply_text("Список задач пуст.")
        return
    lines = [f"{i + 1}. {item}" for i, item in enumerate(tasks)]
    await update.message.reply_text("\n".join(lines))


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("task", add_task))
    app.add_handler(CommandHandler("list", list_tasks))
    app.run_polling()


if __name__ == "__main__":
    main()
