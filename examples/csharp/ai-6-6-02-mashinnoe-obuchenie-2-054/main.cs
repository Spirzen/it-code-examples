using Microsoft.ML;
using Microsoft.ML.Data;
using Microsoft.ML.Trainers;
using System;
using System.Collections.Generic;
using System.Linq;

public class TransactionData
{
    [LoadColumn(0)] public float Amount;
    [LoadColumn(1)] public float Time;
    [LoadColumn(2)] public float V1;
    [LoadColumn(3)] public float V2;
    [LoadColumn(4)] public float V3;
    [LoadColumn(5)] public bool Label; // true - мошенничество, false - нормальная транзакция
}

public class TransactionPrediction
{
    [ColumnName("PredictedLabel")] public bool Prediction;
    public float Probability;
    public float Score;
}

// Создание контекста ML.NET
var mlContext = new MLContext(seed: 42);

// Загрузка данных (пример с синтетическими данными)
var dataView = mlContext.Data.LoadFromEnumerable(GetSyntheticData());

// Разделение на обучающую и тестовую выборки
var splitDataView = mlContext.Data.TrainTestSplit(dataView, testFraction: 0.2);

// Создание конвейера с взвешиванием классов
var pipeline = mlContext.Transforms.Concatenate("Features", 
    "Amount", "Time", "V1", "V2", "V3")
    .Append(mlContext.BinaryClassification.Trainers.SdcaLogisticRegression(
        new SdcaLogisticRegressionBinaryTrainer.Options
        {
            LabelColumnName = "Label",
            FeatureColumnName = "Features",
            ExampleWeightColumnName = "Weight" // колонка с весами примеров
        }));

// Добавление весов для балансировки классов
var weightedData = mlContext.Data.ApplyOnEnumerable(splitDataView.TrainSet, AddWeights);

// Обучение модели
var model = pipeline.Fit(weightedData);

// Оценка качества
var predictions = model.Transform(splitDataView.TestSet);
var metrics = mlContext.BinaryClassification.Evaluate(predictions, labelColumnName: "Label");

Console.WriteLine($"Точность: {metrics.Accuracy:F4}");
Console.WriteLine($"Полнота (миноритарный класс): {metrics.Recall:F4}");
Console.WriteLine($"F1-мера: {metrics.F1Score:F4}");

// Метод генерации синтетических данных
IEnumerable<TransactionData> GetSyntheticData()
{
    var random = new Random(42);
    var transactions = new List<TransactionData>();
    
    // 9900 нормальных транзакций
    for (int i = 0; i < 9900; i++)
    {
        transactions.Add(new TransactionData
        {
            Amount = (float)(random.NextDouble() * 1000),
            Time = (float)(random.NextDouble() * 86400),
            V1 = (float)random.NextDouble(),
            V2 = (float)random.NextDouble(),
            V3 = (float)random.NextDouble(),
            Label = false
        });
    }
    
    // 100 мошеннических транзакций
    for (int i = 0; i < 100; i++)
    {
        transactions.Add(new TransactionData
        {
            Amount = (float)(random.NextDouble() * 5000 + 1000), // обычно крупнее
            Time = (float)(random.NextDouble() * 86400),
            V1 = (float)(random.NextDouble() + 0.5),
            V2 = (float)(random.NextDouble() + 0.5),
            V3 = (float)(random.NextDouble() + 0.5),
            Label = true
        });
    }
    
    return transactions;
}

// Метод добавления весов для балансировки
IEnumerable<(TransactionData row, float Weight)> AddWeights(IDataView dataView)
{
    var enumerable = mlContext.Data.CreateEnumerable<TransactionData>(dataView, reuseRowObject: false);
    var totalCount = enumerable.Count();
    var fraudCount = enumerable.Count(x => x.Label);
    var normalCount = totalCount - fraudCount;
    
    var fraudWeight = (float)totalCount / (2 * fraudCount);
    var normalWeight = (float)totalCount / (2 * normalCount);
    
    foreach (var item in enumerable)
    {
        yield return (item, item.Label ? fraudWeight : normalWeight);
    }
}
