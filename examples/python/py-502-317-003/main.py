SURVEY: dict[int, dict] = {}  # chat_id → промежуточные ответы

@bot.message_handler(commands=["survey"])
def survey_start(message):
    msg = bot.reply_to(message, "Как вас зовут?")
    bot.register_next_step_handler(msg, survey_age)

def survey_age(message):
    name = (message.text or "").strip()
    if len(name) < 2:
        msg = bot.reply_to(message, "Имя слишком короткое. Введите ещё раз:")
        bot.register_next_step_handler(msg, survey_age)
        return
    SURVEY[message.chat.id] = {"name": name}
    msg = bot.reply_to(message, "Сколько вам лет?")
    bot.register_next_step_handler(msg, survey_finish)

def survey_finish(message):
    if not message.text or not message.text.isdigit():
        bot.reply_to(message, "Введите возраст числом.")
        return
    data = SURVEY.get(message.chat.id, {})
    bot.reply_to(message, f"Спасибо, {data.get('name')}! Возраст: {message.text}.")
