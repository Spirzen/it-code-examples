using System.Net.Http.Json;
using System.Text.Json;

public sealed class CatalogClient
{
    private readonly HttpClient _http;
    private static readonly JsonSerializerOptions JsonOpts = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        PropertyNameCaseInsensitive = true,
    };

    public CatalogClient(HttpClient http) => _http = http;

    public async Task<CatalogProductDto?> GetProductAsync(string productId, CancellationToken ct)
    {
        var resp = await _http.GetAsync($"/api/v1/products/{productId}", ct);
        if (resp.StatusCode == System.Net.HttpStatusCode.NotFound) return null;
        resp.EnsureSuccessStatusCode();
        return await resp.Content.ReadFromJsonAsync<CatalogProductDto>(JsonOpts, ct);
    }

    public async Task<CatalogReservationDto> ReserveAsync(
        string productId, int quantity, string orderRef, string idempotencyKey, CancellationToken ct)
    {
        using var req = new HttpRequestMessage(HttpMethod.Post, "/api/v1/reservations");
        req.Headers.Add("Idempotency-Key", idempotencyKey);
        req.Content = JsonContent.Create(new
        {
            productId,
            quantity,
            orderRef,
        }, options: JsonOpts);

        var resp = await _http.SendAsync(req, ct);
        if ((int)resp.StatusCode == 409)
            throw new InsufficientStockException(productId);
        resp.EnsureSuccessStatusCode();
        return (await resp.Content.ReadFromJsonAsync<CatalogReservationDto>(JsonOpts, ct))!;
    }
}
