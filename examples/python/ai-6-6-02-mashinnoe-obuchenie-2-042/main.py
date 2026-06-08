
import tensorflow as tf

from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Загрузка предобученной базы без выходного слоя
base_model = EfficientNetB0(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Замораживание ранних слоёв
for layer in base_model.layers[:200]:
    layer.trainable = False

# Построение головы классификации
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(10, activation='softmax')(x)  # 10 классов

model = Model(inputs=base_model.input, outputs=predictions)

# Компиляция модели
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Подготовка генераторов данных с аугментацией
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Пример использования (требует реальных данных в папках)
# train_generator = train_datagen.flow_from_directory(
#     'data/train',
#     target_size=(224, 224),
#     batch_size=32,
#     class_mode='categorical'
# )
# 
# validation_generator = test_datagen.flow_from_directory(
#     'data/validation',
#     target_size=(224, 224),
#     batch_size=32,
#     class_mode='categorical'
# )
# 
# model.fit(
#     train_generator,
#     epochs=15,
#     validation_data=validation_generator
# )

# Второй этап — размораживание части слоёв для полной тонкой настройки
for layer in base_model.layers:
    layer.trainable = True

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Продолжение обучения с малой скоростью
# model.fit(
#     train_generator,
#     epochs=10,
#     validation_data=validation_generator
# )
