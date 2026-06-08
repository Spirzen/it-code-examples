using Microsoft.ML;
using Microsoft.ML.Data;

public class CustomerData
{
    [LoadColumn(0)] public float Age;
    [LoadColumn(1)] public float Income;
    [LoadColumn(2)] public float PurchaseFrequency;
    [LoadColumn(3)] public bool ChurnRisk;
}

var mlContext = new MLContext(seed: 42);
var dataView = mlContext.Data.LoadFromTextFile<CustomerData>("customer_data.csv", separatorChar: ',');

var trainTestSplit = mlContext.Data.TrainTestSplit(dataView, testSize: 0.2);
var pipeline = mlContext.BinaryClassification.Trainers.SdcaLogisticRegression(
    labelColumnName: nameof(CustomerData.ChurnRisk),
    featureColumnName: "Features"
);

var trainedModel = pipeline.Fit(trainTestSplit.TrainSet);
var predictions = trainedModel.Transform(trainTestSplit.TestSet);
var metrics = mlContext.BinaryClassification.Evaluate(predictions);
Console.WriteLine($"Точность: {metrics.Accuracy:F2}");
