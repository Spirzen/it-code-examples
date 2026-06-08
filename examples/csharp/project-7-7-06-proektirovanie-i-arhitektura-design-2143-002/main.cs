public class ValidationBehaviour<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
    where TRequest : notnull
{
  private readonly IEnumerable<IValidator<TRequest>> _validators;

  public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, CancellationToken ct)
  {
    if (_validators.Any())
    {
      var results = await Task.WhenAll(
        _validators.Select(v => v.ValidateAsync(new ValidationContext<TRequest>(request), ct)));
      var failures = results.SelectMany(r => r.Errors).Where(e => e != null).ToList();
      if (failures.Count != 0)
        throw new ValidationException(failures);
    }
    return await next();
  }
}
