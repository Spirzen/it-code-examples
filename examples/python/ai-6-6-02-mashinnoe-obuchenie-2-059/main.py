
import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader

import albumentations as A

from albumentations.pytorch import ToTensorV2

import numpy as np
import cv2
import os

# Синтетический датасет для демонстрации
class SyntheticSegmentationDataset(Dataset):
    def __init__(self, size=1000, transform=None):
        self.size = size
        self.transform = transform
        self.shapes = ['circle', 'rectangle', 'triangle']
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        # Генерация синтетического изображения с фигурами
        img = np.zeros((256, 256, 3), dtype=np.uint8)
        mask = np.zeros((256, 256), dtype=np.uint8)
        
        # Случайное количество фигур
        n_shapes = np.random.randint(1, 4)
        for _ in range(n_shapes):
            shape_type = np.random.choice(self.shapes)
            color = np.random.randint(50, 255, 3).tolist()
            x, y = np.random.randint(50, 200, 2)
            size = np.random.randint(20, 60)
            
            if shape_type == 'circle':
                cv2.circle(img, (x, y), size, color, -1)
                cv2.circle(mask, (x, y), size, 1, -1)
            elif shape_type == 'rectangle':
                cv2.rectangle(img, (x-size, y-size), (x+size, y+size), color, -1)
                cv2.rectangle(mask, (x-size, y-size), (x+size, y+size), 1, -1)
            else:  # triangle
                pts = np.array([[x, y-size], [x-size, y+size], [x+size, y+size]], np.int32)
                cv2.fillPoly(img, [pts], color)
                cv2.fillPoly(mask, [pts], 1)
        
        if self.transform:
            augmented = self.transform(image=img, mask=mask)
            img = augmented['image']
            mask = augmented['mask']
        
        return img, mask.long()

# Аугментации и нормализация
train_transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

val_transform = A.Compose([
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

# Создание датасетов
train_dataset = SyntheticSegmentationDataset(size=800, transform=train_transform)
val_dataset = SyntheticSegmentationDataset(size=200, transform=val_transform)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=4)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False, num_workers=4)

# Загрузка предобученной модели U-Net

import segmentation_models_pytorch as smp

model = smp.Unet(
    encoder_name="resnet34",
    encoder_weights="imagenet",
    in_channels=3,
    classes=2  # фон + объект
)

# Функция потерь Dice + кросс-энтропия
class DiceLoss(nn.Module):
    def __init__(self, smooth=1.0):
        super(DiceLoss, self).__init__()
        self.smooth = smooth
    
    def forward(self, logits, targets):
        probs = torch.sigmoid(logits)
        intersection = (probs * targets).sum()
        dice = (2. * intersection + self.smooth) / (probs.sum() + targets.sum() + self.smooth)
        return 1 - dice

dice_loss = DiceLoss()
bce_loss = nn.BCEWithLogitsLoss()

def combined_loss(logits, targets):
    return dice_loss(logits, targets) + bce_loss(logits, targets.float())

# Обучение модели
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-4)

for epoch in range(15):
    model.train()
    train_loss = 0.0
    
    for images, masks in train_loader:
        images = images.to(device)
        masks = masks.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = combined_loss(outputs, masks)
        loss.backward()
        optimizer.step()
        
        train_loss += loss.item()
    
    # Валидация
    model.eval()
    val_loss = 0.0
    
    with torch.no_grad():
        for images, masks in val_loader:
            images = images.to(device)
            masks = masks.to(device)
            outputs = model(images)
            loss = combined_loss(outputs, masks)
            val_loss += loss.item()
    
    print(f"Эпоха {epoch+1}: потери обучения {train_loss/len(train_loader):.4f}, "
          f"потери валидации {val_loss/len(val_loader):.4f}")

# Визуализация результатов сегментации

import matplotlib.pyplot as plt

model.eval()
images, masks = next(iter(val_loader))
images = images.to(device)
with torch.no_grad():
    outputs = model(images)
    preds = (torch.sigmoid(outputs) > 0.5).float()

# Отображение первых 4 изображений из батча
fig, axes = plt.subplots(4, 3, figsize=(12, 16))
for i in range(4):
    # Исходное изображение
    img = images[i].cpu().permute(1, 2, 0).numpy()
    img = img * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406])
    img = np.clip(img, 0, 1)
    axes[i, 0].imshow(img)
    axes[i, 0].set_title('Исходное изображение')
    axes[i, 0].axis('off')
    
    # Истинная маска
    axes[i, 1].imshow(masks[i].cpu().numpy(), cmap='gray')
    axes[i, 1].set_title('Истинная маска')
    axes[i, 1].axis('off')
    
    # Предсказанная маска
    axes[i, 2].imshow(preds[i][0].cpu().numpy(), cmap='gray')
    axes[i, 2].set_title('Предсказанная маска')
    axes[i, 2].axis('off')

plt.tight_layout()
plt.savefig('segmentation_results.png')
plt.close()
