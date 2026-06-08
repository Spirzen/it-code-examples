// Многослойный перцептрон на Java с Deeplearning4j

import org.deeplearning4j.nn.conf.MultiLayerConfiguration;
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.learning.config.Adam;
import org.nd4j.linalg.lossfunctions.LossFunctions;

MultiLayerConfiguration conf = new NeuralNetConfiguration.Builder()
    .updater(new Adam(0.001))
    .list()
    .layer(new DenseLayer.Builder().nIn(30).nOut(64).activation(Activation.RELU).build())
    .layer(new DenseLayer.Builder().nIn(64).nOut(32).activation(Activation.RELU).build())
    .layer(new DenseLayer.Builder().nIn(32).nOut(16).activation(Activation.RELU).build())
    .layer(new OutputLayer.Builder(LossFunctions.LossFunction.MSE).nIn(16).nOut(1).activation(Activation.SIGMOID).build())
    .build();

MultiLayerNetwork model = new MultiLayerNetwork(conf);
model.init();
