
import numpy as np

def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array(
    [
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ],
    dtype=float,
)
y = np.array([[0, 0, 0, 0, 1, 1, 1, 1]], dtype=float).T

ITERATIONS = 10_000
np.random.seed(1)
syn0 = 2 * np.random.random((4, 1)) - 1

for _ in range(ITERATIONS):
    l1 = nonlin(X.dot(syn0))
    syn0 += X.T.dot((y - l1) * nonlin(l1, deriv=True))

print("После обучения на X:")
print(np.round(nonlin(X.dot(syn0)).flatten(), 4))

for label, vec in [
    ("похож на 0", [0, 1, 0, 1]),
    ("похож на 1", [1, 1, 1, 1]),
    ("чужой", [0, 0, 0, 0]),
]:
    print(label, np.round(nonlin(np.dot(vec, syn0)).item(), 4))
