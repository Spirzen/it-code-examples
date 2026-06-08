using Microsoft.ML;
using Microsoft.ML.Transforms;

var mlContext = new MLContext();
var pipeline = mlContext.Transforms.Text featurizeText(
    "Features", 
    "Text"
);

var data = mlContext.Data.LoadFromEnumerable(new[]
{
    new { Text = "Кошки спят большую часть дня" },
    new { Text = "Собаки любят гулять на улице" }
});

var model = pipeline.Fit(data);
var transformedData = model.Transform(data);
