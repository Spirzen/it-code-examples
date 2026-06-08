def solar_system():
    # Солнце
    t.penup(); t.goto(0, 0); t.dot(50, "yellow")
    
    # Планеты по орбитам
    orbits = [
        (30, "gray", 0.02),     # Меркурий
        (50, "tan", 0.015),     # Венера
        (75, "blue", 0.01),     # Земля
        (100, "red", 0.008),    # Марс
    ]
    
    angles = [0, 45, 90, 135]
    for i, (r, color, speed) in enumerate(orbits):
        angle = angles[i]
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        t.penup(); t.goto(x, y)
        t.dot(10, color)
        angles[i] += speed * 180 / math.pi  # обновление угла
