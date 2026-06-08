import matplotlib.pyplot as plt
import numpy as np

groups = ["Q1", "Q2", "Q3", "Q4"]
team_a = [12, 19, 14, 22]
team_b = [10, 16, 18, 20]

x = np.arange(len(groups))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width / 2, team_a, width, label="Команда A")
ax.bar(x + width / 2, team_b, width, label="Команда B")
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylabel("Закрытые задачи")
ax.set_title("Квартальная динамика")
ax.legend()
plt.show()
