public class OverdueNotificationService : BackgroundService
{
    private readonly IServiceProvider _serviceProvider;
    private readonly ILogger<OverdueNotificationService> _logger;

    public OverdueNotificationService(IServiceProvider serviceProvider, ILogger<OverdueNotificationService> logger)
    {
        _serviceProvider = serviceProvider;
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            using var scope = _serviceProvider.CreateScope();
            var context = scope.ServiceProvider.GetRequiredService<LibraryContext>();
            var notificationService = scope.ServiceProvider.GetRequiredService<INotificationService>();

            var overdueLoans = await context.Loans
                .Where(l => !l.IsReturned && l.IssueDate.AddDays(14) < DateTime.UtcNow)
                .Include(l => l.Reader)
                .ToListAsync(stoppingToken);

            foreach (var loan in overdueLoans)
            {
                await notificationService.SendEmailAsync(
                    loan.Reader.Email,
                    "Напоминание о возврате книги",
                    $"Уважаемый {loan.Reader.FullName}, пожалуйста, верните книгу "{loan.Book.Title}"."
                );
            }

            await Task.Delay(TimeSpan.FromHours(24), stoppingToken);
        }
    }
}
