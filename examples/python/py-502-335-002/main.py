"""Обучение модели и сохранение весов в models/digit_cnn.pt"""

from pathlib import Path
from typing import Callable

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms

from model import DigitCNN

MODEL_PATH = Path(__file__).parent / "models" / "digit_cnn.pt"
EPOCHS = 2
BATCH_SIZE = 128
LEARNING_RATE = 1e-3
TRAIN_SAMPLES = 20_000


def train(on_progress: Callable[[str], None] | None = None) -> Path:
    def report(message: str) -> None:
        if on_progress:
            on_progress(message)
        else:
            print(message)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    report(f"Устройство: {device}")

    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ]
    )

    dataset = datasets.MNIST(root="data", train=True, download=True, transform=transform)
    subset = Subset(dataset, range(min(TRAIN_SAMPLES, len(dataset))))
    train_loader = DataLoader(subset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)

    model = DigitCNN().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    criterion = nn.CrossEntropyLoss()

    model.train()
    for epoch in range(EPOCHS):
        total_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * images.size(0)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
            total += labels.size(0)

        accuracy = 100.0 * correct / total
        avg_loss = total_loss / total
        report(f"Эпоха {epoch + 1}/{EPOCHS} — loss: {avg_loss:.4f}, accuracy: {accuracy:.2f}%")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), MODEL_PATH)
    report(f"Модель сохранена: {MODEL_PATH}")
    return MODEL_PATH


if __name__ == "__main__":
    train()
