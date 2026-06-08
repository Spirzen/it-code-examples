import torch

# y ≈ w * x, одна обучаемая переменная
x = torch.tensor([1.0, 2.0, 3.0])
y_true = torch.tensor([2.0, 4.0, 6.0])
w = torch.tensor(0.0, requires_grad=True)
lr = 0.1

for _ in range(50):
    y_pred = w * x
    loss = ((y_pred - y_true) ** 2).mean()
    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
    w.grad.zero_()

print(w.item())  # близко к 2.0
