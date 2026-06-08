
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms

from torchvision import models

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# Контрастные аугментации изображений
class ContrastiveTransformations:
    def __init__(self, size=224):
        self.transform = transforms.Compose([
            transforms.RandomResizedCrop(size=size, scale=(0.2, 1.0)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomApply([
                transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1)
            ], p=0.8),
            transforms.RandomGrayscale(p=0.2),
            transforms.GaussianBlur(kernel_size=23, sigma=(0.1, 2.0)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    
    def __call__(self, x):
        return self.transform(x), self.transform(x)

# Симметричная архитектура контрастного обучения
class SimCLR(nn.Module):
    def __init__(self, base_encoder, hidden_dim=2048, out_dim=128):
        super(SimCLR, self).__init__()
        
        # Базовый энкодер (без классификационной головы)
        self.encoder = nn.Sequential(*list(base_encoder.children())[:-1])
        
        # Голова проекции
        self.projection = nn.Sequential(
            nn.Linear(2048, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim)
        )
    
    def forward(self, x):
        # Извлечение признаков
        h = self.encoder(x)
        h = h.view(h.size(0), -1)
        
        # Проекция в пространство сравнения
        z = self.projection(h)
        
        # Нормализация представлений
        z = F.normalize(z, dim=1)
        return z

# Функция потерь контрастного обучения
class NT_XentLoss(nn.Module):
    def __init__(self, temperature=0.5):
        super(NT_XentLoss, self).__init__()
        self.temperature = temperature
    
    def forward(self, z_i, z_j):
        batch_size = z_i.size(0)
        
        # Объединение представлений в один тензор
        z = torch.cat([z_i, z_j], dim=0)
        
        # Матрица сходства
        sim_matrix = torch.mm(z, z.t()) / self.temperature
        
        # Маска для исключения самосравнения
        mask = torch.eye(2 * batch_size, dtype=torch.bool).to(z.device)
        sim_matrix.masked_fill_(mask, -9e9)
        
        # Индексы положительных пар
        pos_indices = torch.arange(batch_size, device=z.device)
        pos_indices_j = pos_indices + batch_size
        pos_indices_i = pos_indices + batch_size
        
        # Логарифм вероятностей
        log_prob = F.log_softmax(sim_matrix, dim=1)
        
        # Потери для пар (i, j) и (j, i)
        loss_i = -log_prob[torch.arange(batch_size), pos_indices_j]
        loss_j = -log_prob[torch.arange(batch_size) + batch_size, pos_indices_i]
        
        loss = (loss_i + loss_j).mean()
        return loss

# Генерация синтетических изображений для демонстрации
def generate_synthetic_images(n_images=100, size=224):
    images = []
    for _ in range(n_images):
        img = np.random.rand(size, size, 3) * 255
        # Добавление структурированных паттернов
        for _ in range(np.random.randint(3, 7)):
            x, y = np.random.randint(0, size, 2)
            radius = np.random.randint(10, 40)
            color = np.random.rand(3)
            for i in range(size):
                for j in range(size):
                    if (i - x)**2 + (j - y)**2 < radius**2:
                        img[i, j] = color * 255
        images.append(Image.fromarray(img.astype(np.uint8)))
    return images

# Создание синтетического датасета
synthetic_images = generate_synthetic_images(n_images=200)
transform = ContrastiveTransformations(size=128)

# Инициализация модели и оптимизатора
base_encoder = models.resnet50(weights=None)
model = SimCLR(base_encoder, hidden_dim=512, out_dim=64)
criterion = NT_XentLoss(temperature=0.5)
optimizer = torch.optim.Adam(model.parameters(), lr=3e-4)

# Обучение контрастной модели
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

print("Обучение контрастной модели...")
train_losses = []

for epoch in range(25):
    epoch_loss = 0.0
    n_batches = 0
    
    for img in synthetic_images[:100]:  # используем подмножество для демонстрации
        # Применение двух аугментаций
        x_i, x_j = transform(img)
        x_i = x_i.unsqueeze(0).to(device)
        x_j = x_j.unsqueeze(0).to(device)
        
        # Прямой проход
        z_i = model(x_i)
        z_j = model(x_j)
        
        # Вычисление потерь
        loss = criterion(z_i, z_j)
        
        # Обратное распространение
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item()
        n_batches += 1
    
    avg_loss = epoch_loss / n_batches
    train_losses.append(avg_loss)
    print(f"Эпоха {epoch+1}: потери {avg_loss:.4f}")

# Визуализация динамики обучения
plt.figure(figsize=(10, 6))
plt.plot(train_losses, marker='o', linewidth=2, markersize=4)
plt.xlabel('Эпоха')
plt.ylabel('Контрастные потери')
plt.title('Динамика контрастного обучения')
plt.grid(True, alpha=0.3)
plt.savefig('contrastive_learning_progress.png')
plt.close()

# Оценка качества представлений
model.eval()
embeddings = []
labels = []

with torch.no_grad():
    for idx, img in enumerate(synthetic_images[100:150]):  # тестовое подмножество
        # Извлечение представления без аугментаций
        transform_simple = transforms.Compose([
            transforms.Resize(128),
            transforms.CenterCrop(128),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        x = transform_simple(img).unsqueeze(0).to(device)
        z = model(x)
        embeddings.append(z.cpu().numpy()[0])
        labels.append(idx // 10)  # группировка по 10 изображений в класс

embeddings = np.array(embeddings)
labels = np.array(labels)

# Визуализация представлений через t-SNE
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42, perplexity=15)
embeddings_2d = tsne.fit_transform(embeddings)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    embeddings_2d[:, 0], 
    embeddings_2d[:, 1],
    c=labels,
    cmap='tab10',
    alpha=0.8,
    s=100
)
plt.colorbar(scatter, label='Группа изображений')
plt.title('Пространство представлений после контрастного обучения')
plt.xlabel('t-SNE компонента 1')
plt.ylabel('t-SNE компонента 2')
plt.grid(True, alpha=0.3)
plt.savefig('contrastive_embeddings.png')
plt.close()

print("Контрастное обучение завершено. Представления демонстрируют кластеризацию по группам изображений.")
