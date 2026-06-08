
import smile.classification.RandomForest;
import smile.Data.DataFrame;
import smile.validation.metric.Accuracy;

// Загрузка данных
DataFrame df = DataFrame.read("data.csv");
double[][] x = df.drop("target").toArray();
int[] y = df.column("target").toIntArray();

// Обучение модели
RandomForest forest = RandomForest.fit(
    x, 
    y, 
    100,      // количество деревьев
    2,        // минимальное количество образцов в листе
    1.0,      // доля бутстрап-выборки
    Math.sqrt(x[0].length) // количество признаков для разбиения
);

// Оценка качества
int[] predictions = forest.predict(x);
double accuracy = Accuracy.of(y, predictions);
