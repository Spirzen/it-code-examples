using System.Net.Http.Headers;
using System.Text;

var credentials = Convert.ToBase64String(
    Encoding.UTF8.GetBytes("svc_erp:secret_from_vault"));
var client = httpClientFactory.CreateClient("ErpPartner");
client.DefaultRequestHeaders.Authorization =
    new AuthenticationHeaderValue("Basic", credentials);

// Альтернатива — встроенный handler (удобно для IIS/legacy)
var handler = new HttpClientHandler
{
    Credentials = new NetworkCredential("svc_erp", "secret_from_vault")
};
