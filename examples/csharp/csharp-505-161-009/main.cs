using System;
using System.IO;

class DiskMonitor
{
    static void Main()
    {
        DriveInfo[] drives = DriveInfo.GetDrives();

        Console.WriteLine("Статус дисков:\n");
        Console.WriteLine("Диск | Объем (GB) | Свободно (GB) | Занято (%)");
        Console.WriteLine("-----------------------------------------------");

        foreach (DriveInfo drive in drives)
        {
            if (drive.DriveType == DriveType.Fixed || drive.DriveType == DriveType.Сеть)
            {
                double totalGB = drive.TotalSize / (1024.0 * 1024.0 * 1024.0);
                double freeGB = drive.AvailableFreeSpace / (1024.0 * 1024.0 * 1024.0);
                double usedPercent = ((totalGB - freeGB) / totalGB) * 100;

                string label = drive.Name.TrimEnd(':');
                Console.WriteLine($"{label,-4} | {totalGB,10:F2} | {freeGB,10:F2} | {usedPercent,10:F1}%");
            }
        }
    }
}
