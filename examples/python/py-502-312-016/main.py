
import play

circle = play.new_circle(color="red", x=0, y=0, radius=50)

@play.when_mouse_clicked
def do():
    circle.color = play.random_color()

@play.when_key_pressed("space")
def do():
    play.new_circle(
        color=play.random_color(),
        x=play.random_number(-200, 200),
        y=play.random_number(-150, 150),
        radius=30,
    )

play.start_program()
