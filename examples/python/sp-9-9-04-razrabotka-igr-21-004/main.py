from mc import *

# Функция для сбора одного слоя
def harvest_layer():
    for i in range(4):
        agent.move(FORWARD, 1)
        agent.destroy(FORWARD)
        agent.collect_all()
    agent.turn(RIGHT)

# Основной цикл — 3 уровня
def on_chat():
    for level in range(3):
        for _ in range(4):
            harvest_layer()
        agent.move(UP, 1)

# Привязка к команде в чате
player.on_chat("farm", on_chat)
