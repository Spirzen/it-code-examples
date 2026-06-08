
import matplotlib.pyplot as plt
import numpy as np

# Создаем данные
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/5) * np.sin(x)

# Создаем фигуру и оси
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Линейный график
axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].plot(x, y2, label='cos(x)', color='red')
axes[0, 0].set_title('Тригонометрические функции')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Гистограмма
data = np.random.randn(1000)
axes[0, 1].hist(data, bins=30, alpha=0.7, color='green')
axes[0, 1].set_title('Гистограмма нормального распределения')
axes[0, 1].set_xlabel('Значение')
axes[0, 1].set_ylabel('Частота')

# Диаграмма рассеяния
x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
axes[1, 0].scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5)
axes[1, 0].set_title('Диаграмма рассеяния')
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('y')

# Столбчатая диаграмма
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
axes[1, 1].bar(categories, values, color='purple', alpha=0.7)
axes[1, 1].set_title('Столбчатая диаграмма')
axes[1, 1].set_xlabel('Категория')
axes[1, 1].set_ylabel('Значение')

plt.tight_layout()
plt.savefig('visualization.png', dpi=300, bbox_inches='tight')
plt.show()
