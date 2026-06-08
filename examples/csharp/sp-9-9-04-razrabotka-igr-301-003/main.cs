public class BuildProcessor : IPreprocessBuildWithReport, IPostprocessBuildWithReport
{
    public int callbackOrder => 0;

    public void OnPreprocessBuild(BuildReport report)
    {
        // Версия, иконки, splash screen
        PlayerSettings.bundleVersion = DateTime.Now.ToString("yy.MM.dd.HH");
    }

    public void OnPostprocessBuild(BuildReport report)
    {
        // Подпись APK, копирование в deploy-папку
        if (report.summary.platform == BuildTarget.Android)
            SignAPK(report.summary.outputPath);
    }
}
