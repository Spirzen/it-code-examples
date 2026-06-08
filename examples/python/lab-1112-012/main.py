import matplotlib.pyplot as plt
import numpy as np

years = np.array([2022, 2023, 2024, 2025])
web = np.array([30, 35, 38, 40])
mobile = np.array([25, 28, 32, 36])
api = np.array([15, 18, 22, 24])

plt.stackplot(
    years,
    web,
    mobile,
    api,
    labels=["Web", "Mobile", "API"],
    alpha=0.85,
)
plt.legend(loc="upper left")
plt.xlabel("Год")
plt.ylabel("Доля трафика, %")
plt.title("Структура трафика во времени")
plt.show()
