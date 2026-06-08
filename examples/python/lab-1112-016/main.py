def setup_figure(
    title: str = "Matplotlib experiment",
    width: float = 8.0,
    height: float = 5.0,
    style: str = "seaborn-v0_8-whitegrid",
) -> tuple:
    import matplotlib.pyplot as plt

    plt.style.use(style)
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_title(title)
    return fig, ax

# Пример использования:
fig, ax = setup_figure("Мой график")
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
