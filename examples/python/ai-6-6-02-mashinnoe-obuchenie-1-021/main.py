
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Устанавливаем стиль
sns.set_style("whitegrid")

# Создаем данные
np.random.seed(42)
data = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'value1': np.random.randn(100),
    'value2': np.random.randn(100) + np.random.choice([0, 2, 4], 100),
    'value3': np.random.rand(100) * 100
})

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value1', data=data)
plt.title('Boxplot по категориям')
plt.xlabel('Категория')
plt.ylabel('Значение')
plt.show()

# Heatmap корреляции
plt.figure(figsize=(8, 6))
correlation = data[['value1', 'value2', 'value3']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Матрица корреляции')
plt.show()

# Pairplot
sns.pairplot(data, hue='category', palette='Set2')
plt.suptitle('Pairplot данных', y=1.02)
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='category', y='value2', data=data, palette='muted')
plt.title('Violin plot по категориям')
plt.xlabel('Категория')
plt.ylabel('Значение')
plt.show()
