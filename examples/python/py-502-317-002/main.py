@bot.message_handler(commands=["quiz"])
def quiz(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Вариант A", callback_data="ans_a"),
        types.InlineKeyboardButton("Вариант B", callback_data="ans_b"),
    )
    bot.send_message(message.chat.id, "Выберите ответ:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("ans_"))
def on_answer(call):
    correct = call.data == "ans_a"
    text = "Верно!" if correct else "Неверно."
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)  # убрать «часики» у кнопки
