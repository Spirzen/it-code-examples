
import tensorflow as tf

from tensorflow.keras import layers, models

model = models.Sequential([
    # Первый свёрточный блок
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Второй свёрточный блок
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Третий свёрточный блок
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Полносвязные слои для классификации
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 классов цифр
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
