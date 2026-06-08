using System.IO;
using Microsoft.Win32;

public sealed class InstallService
{
    private const string UninstallKeyPath =
        @"Software\Microsoft\Windows\CurrentVersion\Uninstall\MyDemoApp";

    public void Install(string sourceDir, string targetDir, string publisher, string version)
    {
        if (!Directory.Exists(sourceDir))
            throw new DirectoryNotFoundException(sourceDir);

        Directory.CreateDirectory(targetDir);
        CopyAll(new DirectoryInfo(sourceDir), new DirectoryInfo(targetDir));

        using var key = Registry.LocalMachine.CreateSubKey(UninstallKeyPath, true);
        key.SetValue("DisplayName", "My Demo App");
        key.SetValue("DisplayVersion", version);
        key.SetValue("Publisher", publisher);
        key.SetValue("InstallLocation", targetDir);
        key.SetValue("UninstallString", $"\"{Path.Combine(targetDir, "uninstall.exe")}\"");
    }

    private static void CopyAll(DirectoryInfo source, DirectoryInfo target)
    {
        target.Create();
        foreach (var file in source.GetFiles())
            file.CopyTo(Path.Combine(target.FullName, file.Name), overwrite: true);
        foreach (var dir in source.GetDirectories())
            CopyAll(dir, target.CreateSubdirectory(dir.Name));
    }
}
