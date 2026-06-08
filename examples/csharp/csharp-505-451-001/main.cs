public interface IPolicy<in TContext>
{
    Task<PolicyResult> EvaluateAsync(TContext context, CancellationToken ct);
}

public sealed class PolicyPipeline<TContext>
{
    private readonly IEnumerable<IPolicy<TContext>> _policies;

    public async Task<PolicyResult> RunAsync(TContext context, CancellationToken ct)
    {
        foreach (var policy in _policies)
        {
            var result = await policy.EvaluateAsync(context, ct);
            if (!result.Success)
                return result;
        }
        return PolicyResult.Ok();
    }
}
