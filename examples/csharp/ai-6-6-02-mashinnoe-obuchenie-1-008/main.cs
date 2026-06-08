// Многослойный перцептрон на C# с TensorFlow.NET
using Tensorflow;
using Tensorflow.Keras.Engine;
using static Tensorflow.KerasApi;

var keras = tf.keras;
var model = keras.Sequential(new Layer[] {
    keras.layers.Dense(64, activation: "relu", input_shape: new int[] { 30 }),
    keras.layers.Dense(32, activation: "relu"),
    keras.layers.Dense(16, activation: "relu"),
    keras.layers.Dense(1, activation: "sigmoid")
});

model.compile(optimizer: "adam", loss: "binary_crossentropy", metrics: new string[] { "accuracy" });
