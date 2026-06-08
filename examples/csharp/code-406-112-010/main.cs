using OpenTelemetry;
using OpenTelemetry.Metrics;
using OpenTelemetry.Trace;

public class Program
{
    public static void Main()
    {
        var tracerProvider = Sdk.CreateTracerProviderBuilder()
            .AddSource("MyApp")
            .AddAspNetCoreInstrumentation()
            .AddHttpClientInstrumentation()
            .AddOtlpExporter()
            .Build();
        
        var meterProvider = Sdk.CreateMeterProviderBuilder()
            .AddMeter("MyApp")
            .AddAspNetCoreInstrumentation()
            .AddOtlpExporter()
            .Build();
    }
}
