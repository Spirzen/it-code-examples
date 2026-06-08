
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Lambda, Layer, Reshape, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K

# Загрузка данных
(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Параметры модели
original_dim = 784
intermediate_dim = 512
latent_dim = 2  # 2D для визуализации

# Слои энкодера
inputs = Input(shape=(original_dim,))
h = Dense(intermediate_dim, activation='relu')(inputs)
z_mean = Dense(latent_dim)(h)
z_log_var = Dense(latent_dim)(h)

# Функция репараметризации
def sampling(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=K.shape(z_mean), mean=0., stddev=1.0)
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

# Слои декодера
decoder_h = Dense(intermediate_dim, activation='relu')
decoder_mean = Dense(original_dim, activation='sigmoid')
h_decoded = decoder_h(z)
x_decoded_mean = decoder_mean(h_decoded)

# Создание моделей
vae = Model(inputs, x_decoded_mean)

# Кастомный слой для вычисления потерь
class VAE_Loss(Layer):
    def __init__(self, **kwargs):
        super(VAE_Loss, self).__init__(**kwargs)
    
    def call(self, inputs):
        x, x_decoded, z_mean, z_log_var = inputs
        xent_loss = original_dim * tf.keras.losses.binary_crossentropy(x, x_decoded)
        kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
        vae_loss = K.mean(xent_loss + kl_loss)
        self.add_loss(vae_loss)
        return x_decoded_mean

outputs = VAE_Loss()([inputs, x_decoded_mean, z_mean, z_log_var])
vae = Model(inputs, outputs)

# Компиляция и обучение
vae.compile(optimizer='adam')
vae.fit(x_train, x_train, shuffle=True, epochs=50, batch_size=128, validation_data=(x_test, x_test))

# Отдельная модель генератора
decoder_input = Input(shape=(latent_dim,))
_h_decoded = decoder_h(decoder_input)
_x_decoded_mean = decoder_mean(_h_decoded)
generator = Model(decoder_input, _x_decoded_mean)

# Визуализация латентного пространства
x_test_encoded = tf.keras.models.Model(inputs, z_mean).predict(x_test, batch_size=128)
plt.figure(figsize=(10, 8))
plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=np.argmax(x_test, axis=1), cmap='tab10')
plt.colorbar()
plt.title('Латентное пространство VAE (MNIST)')
plt.xlabel('z[0]')
plt.ylabel('z[1]')
plt.savefig('vae_latent_space.png')
plt.close()

# Генерация изображений по сетке латентного пространства
n = 15
digit_size = 28
figure = np.zeros((digit_size * n, digit_size * n))

grid_x = np.linspace(-3, 3, n)
grid_y = np.linspace(-3, 3, n)[::-1]

for i, yi in enumerate(grid_y):
    for j, xi in enumerate(grid_x):
        z_sample = np.array([[xi, yi]])
        x_decoded = generator.predict(z_sample, verbose=0)
        digit = x_decoded[0].reshape(digit_size, digit_size)
        figure[i * digit_size: (i + 1) * digit_size,
               j * digit_size: (j + 1) * digit_size] = digit

plt.figure(figsize=(10, 10))
plt.imshow(figure, cmap='gray')
plt.title('Генерация изображений по латентному пространству')
plt.axis('off')
plt.savefig('vae_generation.png')
plt.close()
