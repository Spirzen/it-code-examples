import matplotlib.pyplot as plt

labels = ["Backend", "Frontend", "DevOps", "Data"]
sizes = [40, 30, 15, 15]
explode = (0.05, 0, 0, 0)

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct="%1.0f%%",
    startangle=90,
    colors=["#4c72b0", "#55a868", "#c44e52", "#8172b3"],
)
plt.title("Распределение задач в команде")
plt.axis("equal")
plt.show()
