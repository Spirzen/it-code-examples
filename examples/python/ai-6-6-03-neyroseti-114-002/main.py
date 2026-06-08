from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

cnn = tf.keras.Sequential([
    Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(2),
    Conv2D(64, 3, activation="relu"),
    MaxPooling2D(2),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax"),
])

cnn.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
cnn.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1, verbose=1)
cnn.evaluate(x_test, y_test, verbose=0)
