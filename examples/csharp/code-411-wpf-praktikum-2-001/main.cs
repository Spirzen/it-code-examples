namespace TaskDesk.Core.Models;

public enum TaskStatus { Todo, InProgress, Done }

public sealed class TaskItem
{
    public Guid Id { get; init; } = Guid.NewGuid();
    public required string Title { get; set; }
    public TaskStatus Status { get; set; } = TaskStatus.Todo;
    public DateTimeOffset CreatedAt { get; init; } = DateTimeOffset.UtcNow;

    public bool IsValid() =>
        !string.IsNullOrWhiteSpace(Title) && Title.Length <= 200;
}
