using System.Text.Json.Serialization;

namespace NotificationService.Models
{
    public class OrderEvent
    {
        [JsonPropertyName("orderId")]
        public int OrderId { get; set; }
        
        [JsonPropertyName("status")]
        public string Status { get; set; }
        
        [JsonPropertyName("timestamp")]
        public string Timestamp { get; set; }
    }
}
