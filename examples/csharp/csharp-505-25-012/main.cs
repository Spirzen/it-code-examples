public class Logger
{
    private string _logFile = "app.log"; // скрыто от внешнего мира

    private void WriteToFile(string message)
    {
        File.AppendAllText(_logFile, message);
    }

    public void Log(string message)
    {
        WriteToFile($"[{DateTime.Now}] {message}");
    }
}
