
import turtle
import math

def iso_project(x: float, y: float, z: float, scale: float = 1.0) -> tuple[float, float]:
    """Изометрическая проекция (углы 30°, 30°, 120°)"""
    iso_x = (x - y) * math.cos(math.radians(30)) * scale
    iso_y = (x + y) * math.sin(math.radians(30)) - z * scale
    return iso_x, iso_y

def draw_iso_tetrahedron(edge: float, origin: tuple[float, float] = (0, 0), fill: bool = False):
    t = turtle.Turtle()
    t.speed(0)
    # Вершины правильного тетраэдра в 3D (центрированы в начале)
    a = edge / math.sqrt(2)
    vertices_3d = [
        ( a,  a,  a),
        ( a, -a, -a),
        (-a,  a, -a),
        (-a, -a,  a)
    ]
    proj = [iso_project(x, y, z, 0.8) for x, y, z in vertices_3d]
    proj = [(px + origin[0], py + origin[1]) for px, py in proj]

    faces = [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]
    for face in faces:
        t.penup()
        t.goto(*proj[face[0]])
        t.pendown()
        for idx in face[1:] + (face[0],):
            t.goto(*proj[idx])
        if fill:
            t.begin_fill()
            for idx in face:
                t.goto(*proj[idx])
            t.end_fill()
    t.hideturtle()

draw_iso_tetrahedron(100)

turtle.done()
