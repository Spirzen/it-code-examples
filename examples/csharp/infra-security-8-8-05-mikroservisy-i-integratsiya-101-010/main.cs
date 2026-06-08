using Microsoft.AspNetCore.Mvc;
using NotificationService.Models;
using System.Text.Json;

[ApiController]
[Route("[controller]")]
public class NotificationController : ControllerBase
{
    private readonly ILogger<NotificationController> _logger;

    public NotificationController(ILogger<NotificationController> logger)
    {
        _logger = logger;
    }

    [HttpPost]
    public IActionResult ReceiveNotification([FromBody] OrderEvent orderEvent)
    {
        _logger.LogInformation($"Received direct notification for order {orderEvent.OrderId} with status {orderEvent.Status}");
        return Ok(new { message = "Notification received" });
    }
}
