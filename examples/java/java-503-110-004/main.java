@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@State(Scope.Thread)
@Fork(value = 2)
@Warmup(iterations = 3)
@Measurement(iterations = 5)
public class LoopVsStreamBenchmark {
    private List<Integer> data;

    @Setup
    public void setup() {
        data = IntStream.range(0, 10_000).boxed().collect(Collectors.toList());
    }

    @Benchmark
    public int sumWithLoop() {
        int sum = 0;
        for (int x : data) sum += x;
        return sum;
    }

    @Benchmark
    public int sumWithStream() {
        return data.stream().mapToInt(Integer::intValue).sum();
    }
}
