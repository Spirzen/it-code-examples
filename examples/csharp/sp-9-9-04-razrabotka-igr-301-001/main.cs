[BurstCompile]
struct SineJob : IJobParallelFor
{
    [ReadOnly] public NativeArray<float> input;
    [WriteOnly] public NativeArray<float> output;
    public float frequency;

    public void Execute(int i)
    {
        output[i] = Mathf.Sin(input[i] * frequency * Mathf.PI * 2.0f);
    }
}

// Использование:
var input = new NativeArray<float>(1000, Allocator.TempJob);
var output = new NativeArray<float>(1000, Allocator.TempJob);
var job = new SineJob { input = input, output = output, frequency = 1.0f };
JobHandle handle = job.Schedule(1000, 64); // 64 — batch size
handle.Complete();
output.Dispose();
input.Dispose();
