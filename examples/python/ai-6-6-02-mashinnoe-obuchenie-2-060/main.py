from ultralytics import YOLO

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка предобученной модели
model = YOLO('yolov8n.pt')  # nano версия для быстрой работы

# Генерация синтетических изображений для демонстрации
def create_synthetic_image():
    img = np.ones((480, 640, 3), dtype=np.uint8) * 240
    
    # Добавление объектов разных классов
    cv2.rectangle(img, (100, 100), (200, 250), (0, 0, 255), -1)  # красный прямоугольник (человек)
    cv2.circle(img, (400, 150), 60, (255, 0, 0), -1)  # синий круг (машина)
    cv2.rectangle(img, (250, 300), (350, 400), (0, 255, 0), -1)  # зелёный прямоугольник (стул)
    
    return img

# Создание набора синтетических изображений
test_images = [create_synthetic_image() for _ in range(5)]

# Детекция объектов на изображениях
results = model(test_images, conf=0.25, iou=0.45)

# Визуализация результатов
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, (img, result) in enumerate(zip(test_images, results)):
    if i >= 5:
        break
    
    # Получение аннотированного изображения
    annotated = result.plot()
    
    axes[i].imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    axes[i].set_title(f'Изображение {i+1}: {len(result.boxes)} объектов')
    axes[i].axis('off')

# Добавление легенды
axes[5].axis('off')
legend_text = "Классы объектов:\n0: человек\n2: машина\n59: стул"
axes[5].text(0.5, 0.5, legend_text, ha='center', va='center', fontsize=12, family='monospace')

plt.tight_layout()
plt.savefig('object_detection_results.png')
plt.close()

# Детальный анализ результатов для первого изображения
first_result = results[0]
boxes = first_result.boxes

print("Детектированные объекты на первом изображении:")
print(f"{'Класс':<15} {'Уверенность':<15} {'Координаты рамки'}")
print("-" * 50)

for box in boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    xyxy = box.xyxy[0].cpu().numpy()
    
    # Картирование индексов классов на названия (упрощённое)
    class_names = {0: 'человек', 2: 'машина', 59: 'стул'}
    cls_name = class_names.get(cls_id, f'класс_{cls_id}')
    
    print(f"{cls_name:<15} {conf:.2%}        [{xyxy[0]:.0f}, {xyxy[1]:.0f}, {xyxy[2]:.0f}, {xyxy[3]:.0f}]")

# Экспорт модели в формат ONNX для развёртывания
model.export(format='onnx', imgsz=640, simplify=True)
print("\nМодель экспортирована в формат ONNX для промышленного использования")
