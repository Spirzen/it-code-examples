public class PayrollIntegrationService : BaseIntegrationService
{
    protected override async Task<string> AcquireTokenAsync(CancellationToken ct)
        => await _payrollAuth.GetTokenAsync(ct);

    protected override HttpRequestMessage PrepareRequest<Request>(Request request)
        => new(HttpMethod.Post, "/v1/payroll/upload")
        {
            Content = JsonContent.Create(request, typeof(Request))
        };

    protected override async Task<PayrollResponse> HandleResponseAsync<PayrollResponse>(
        HttpResponseMessage response, CancellationToken ct)
    {
        // switch по статус-кодам, десериализация и т.д.
    }
}
