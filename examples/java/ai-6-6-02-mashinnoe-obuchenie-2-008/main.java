
import weka.classifiers.functions.Logistic;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

// Загрузка данных
DataSource source = new DataSource("data.arff");
Instances data = source.getDataSet();
data.setClassIndex(data.numAttributes() - 1);

// Создание и обучение модели
Logistic logistic = new Logistic();
logistic.setRidge(1.0); // L2 регуляризация
logistic.buildClassifier(data);

// Получение коэффициентов
double[] coefficients = logistic.coefficients();
