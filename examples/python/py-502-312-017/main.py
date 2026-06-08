
import play

# Создание объектов
paddle = play.new_box(color="green", x=0, y=-200, width=100, height=20)
ball = play.new_circle(color="red", x=0, y=200, radius=20)
score = play.new_text(words="Счёт: 0", x=0, y=250)

count = 0

@play.repeat_forever
def do():
    global count

    # Управление платформой
    if play.key_is_pressed("left"):
        paddle.x -= 5
    if play.key_is_pressed("right"):
        paddle.x += 5

    # Движение шарика
    ball.y -= 3

    # Проверка коллизии
    if ball.is_touching(paddle):
        ball.y = 200  # Переместить шарик наверх
        count += 1
        score.words = f"Счёт: {count}"

    # Перезапуск, если шарик упал
    if ball.y < -250:
        ball.y = 200
        count = max(0, count - 1)
        score.words = f"Счёт: {count}"

play.start_program()
