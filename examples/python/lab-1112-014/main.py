import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

start = datetime(2025, 1, 1)
dates = [start + timedelta(days=i) for i in range(30)]
values = np.cumsum(np.random.default_rng(3).normal(0, 1, 30)) + 100

fig, ax = plt.subplots()
ax.plot(dates, values, marker=".")
fig.autofmt_xdate()
ax.set_title("Временной ряд")
ax.set_ylabel("Метрика")
ax.grid(True, alpha=0.3)
plt.show()
