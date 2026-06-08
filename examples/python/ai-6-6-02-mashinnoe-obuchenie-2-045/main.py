# Модификация для условной генерации
def build_conditional_generator():
    noise = tf.keras.Input(shape=(latent_dim,))
    label = tf.keras.Input(shape=(10,))  # 10 классов цифр
    
    merged = tf.keras.layers.Concatenate()([noise, label])
    
    x = Dense(256)(merged)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    x = Dense(512)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    x = Dense(1024)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    output = Dense(784, activation='tanh')(x)
    
    return Model([noise, label], output)

def build_conditional_discriminator():
    image = tf.keras.Input(shape=(784,))
    label = tf.keras.Input(shape=(10,))
    
    merged = tf.keras.layers.Concatenate()([image, label])
    
    x = Dense(512)(merged)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.3)(x)
    
    x = Dense(256)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.3)(x)
    
    output = Dense(1, activation='sigmoid')(x)
    
    return Model([image, label], output)

# Подготовка меток в one-hot формате
from tensorflow.keras.utils import to_categorical
(_, y_train), (_, _) = mnist.load_data()
y_train_cat = to_categorical(y_train, 10)

# Обучение условной GAN аналогично базовой, с передачей меток
# генератору и дискриминатору на каждом шаге
