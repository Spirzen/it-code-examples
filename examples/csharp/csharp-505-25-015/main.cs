public class Logger
{
    private static readonly string _logPath;

    static Logger()
    {
        _logPath = Path.Combine(Environment.CurrentDirectory, "logs.txt");
        Directory.CreateDirectory(Path.GetDirectoryName(_logPath));
    }

    public static void Log(string message)
    {
        File.AppendAllText(_logPath, $"{DateTime.Now}: {message}\n");
    }
}
