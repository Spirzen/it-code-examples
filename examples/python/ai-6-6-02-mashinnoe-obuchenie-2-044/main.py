
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Reshape, Flatten, LeakyReLU, BatchNormalization, Dropout
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

# Загрузка и подготовка данных
(x_train, _), (_, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_train = x_train.reshape(-1, 784)

# Параметры модели
latent_dim = 100
batch_size = 128
epochs = 20000
steps_per_epoch = x_train.shape[0] // batch_size

# Построение генератора
def build_generator():
    model = Sequential([
        Dense(256, input_dim=latent_dim),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(512),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(1024),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(784, activation='tanh')
    ])
    return model

# Построение дискриминатора
def build_discriminator():
    model = Sequential([
        Dense(512, input_dim=784),
        LeakyReLU(alpha=0.2),
        Dropout(0.3),
        Dense(256),
        LeakyReLU(alpha=0.2),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    return model

# Создание моделей
generator = build_generator()
discriminator = build_discriminator()
discriminator.compile(
    optimizer=Adam(learning_rate=0.0002, beta_1=0.5),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Составная модель для обучения генератора
noise_input = tf.keras.Input(shape=(latent_dim,))
generated_image = generator(noise_input)
discriminator.trainable = False
validity = discriminator(generated_image)
combined = Model(noise_input, validity)
combined.compile(
    optimizer=Adam(learning_rate=0.0002, beta_1=0.5),
    loss='binary_crossentropy'
)

# Цикл обучения
for epoch in range(epochs):
    # Обучение дискриминатора
    idx = np.random.randint(0, x_train.shape[0], batch_size)
    real_images = x_train[idx]
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    fake_images = generator.predict(noise, verbose=0)
    
    real_labels = np.ones((batch_size, 1)) * 0.9  # label smoothing
    fake_labels = np.zeros((batch_size, 1))
    
    d_loss_real = discriminator.train_on_batch(real_images, real_labels)
    d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    # Обучение генератора
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    valid_labels = np.ones((batch_size, 1))
    g_loss = combined.train_on_batch(noise, valid_labels)
    
    # Вывод прогресса и сохранение изображений
    if epoch % 1000 == 0:
        print(f"Эпоха {epoch}: потери дискриминатора {d_loss[0]:.4f}, "
              f"точность {100*d_loss[1]:.2f}%, потери генератора {g_loss:.4f}")
        
        noise = np.random.normal(0, 1, (25, latent_dim))
        gen_imgs = generator.predict(noise, verbose=0)
        gen_imgs = 0.5 * gen_imgs + 0.5  # масштабирование в [0, 1]
        
        fig, axs = plt.subplots(5, 5, figsize=(8, 8))
        cnt = 0
        for i in range(5):
            for j in range(5):
                axs[i, j].imshow(gen_imgs[cnt].reshape(28, 28), cmap='gray')
                axs[i, j].axis('off')
                cnt += 1
        plt.tight_layout()
        plt.savefig(f'gan_epoch_{epoch}.png')
        plt.close()
