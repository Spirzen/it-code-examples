import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
(line,) = ax.plot(x, np.sin(x))
ax.set_ylim(-1.2, 1.2)
ax.grid(True, alpha=0.3)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return (line,)

anim = FuncAnimation(fig, update, frames=120, interval=50, blit=True)
plt.show()
