using System;
using System.Diagnostics;

class ProcessViewer
{
    static void Main()
    {
        Process[] processes = Process.GetProcesses();

        Console.WriteLine($"Активных процессов: {processes.Length}\n");
        Console.WriteLine("PID      | Имя процесса       | Время CPU (сек)");
        Console.WriteLine("--------------------------------------------------");

        // Ограничиваем вывод первыми 20 процессами для читаемости
        int count = 0;
        foreach (Process proc in processes)
        {
            if (count >= 20) break;

            try
            {
                string name = proc.ProcessName;
                long cpuSeconds = (long)(proc.TotalProcessorTime.TotalSeconds);
                int pid = proc.Id;

                Console.WriteLine($"{pid,-8} | {name,-18} | {cpuSeconds}");
            }
            catch (InvalidOperationException)
            {
                // Процесс завершился до чтения данных
                continue;
            }
            catch (System.ComponentModel.Win32Exception)
            {
                // Нет прав доступа к процессу
                continue;
            }

            count++;
        }
    }
}
