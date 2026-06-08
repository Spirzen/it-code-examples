
import torch
import torch.nn as nn
import torchvision

from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator

# Создание энкодера на основе ResNet
backbone = torchvision.models.resnet50(weights=torchvision.models.ResNet50_Weights.IMAGENET1K_V1)
modules = list(backbone.children())[:-2]  # Удаление полносвязных слоёв и адаптивного пулинга
backbone = nn.Sequential(*modules)
backbone.out_channels = 2048

# Настройка генератора якорей
anchor_generator = AnchorGenerator(
    sizes=((32, 64, 128, 256, 512),),
    aspect_ratios=((0.5, 1.0, 2.0),)
)

# ROI пулер для извлечения признаков регионов
roi_pooler = torchvision.ops.MultiScaleRoIAlign(
    featmap_names=['0'],
    output_size=7,
    sampling_ratio=2
)

# Создание модели Faster R-CNN
model = FasterRCNN(
    backbone=backbone,
    num_classes=3,  # фон + 2 класса объектов
    rpn_anchor_generator=anchor_generator,
    box_roi_pool=roi_pooler
)

# Подготовка синтетических данных для обучения
def generate_synthetic_detection_data(n_samples=100):
    images = []
    targets = []
    
    for _ in range(n_samples):
        # Создание изображения с фоном
        img = torch.rand(3, 256, 256)
        images.append(img)
        
        # Генерация случайных ограничивающих рамок
        n_boxes = torch.randint(1, 4, (1,)).item()
        boxes = torch.zeros((n_boxes, 4))
        labels = torch.zeros((n_boxes,), dtype=torch.int64)
        
        for i in range(n_boxes):
            x1 = torch.randint(20, 150, (1,)).item()
            y1 = torch.randint(20, 150, (1,)).item()
            x2 = x1 + torch.randint(30, 100, (1,)).item()
            y2 = y1 + torch.randint(30, 100, (1,)).item()
            
            boxes[i] = torch.tensor([x1, y1, x2, y2], dtype=torch.float)
            labels[i] = torch.randint(1, 3, (1,)).item()  # классы 1 и 2
        
        targets.append({
            'boxes': boxes,
            'labels': labels
        })
    
    return images, targets

# Обучение модели
images, targets = generate_synthetic_detection_data(50)
model.train()

params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)

for epoch in range(10):
    loss_dict = model(images, targets)
    losses = sum(loss for loss in loss_dict.values())
    
    optimizer.zero_grad()
    losses.backward()
    optimizer.step()
    
    print(f"Эпоха {epoch+1}: общие потери {losses.item():.4f}, "
          f"потери классификации RPN {loss_dict['loss_objectness'].item():.4f}, "
          f"потери регрессии рамок {loss_dict['loss_box_reg'].item():.4f}")

# Инференс на новых данных
model.eval()
test_image = torch.rand(1, 3, 256, 256)
with torch.no_grad():
    predictions = model(test_image)

print(f"\nОбнаружено объектов: {len(predictions[0]['boxes'])}")
for i, (box, label, score) in enumerate(zip(
    predictions[0]['boxes'],
    predictions[0]['labels'],
    predictions[0]['scores']
)):
    if score > 0.5:
        print(f"Объект {i+1}: класс {label.item()}, уверенность {score.item():.2%}, "
              f"рамка [{box[0]:.0f}, {box[1]:.0f}, {box[2]:.0f}, {box[3]:.0f}]")
