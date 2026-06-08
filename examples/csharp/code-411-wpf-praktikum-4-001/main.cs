public partial class App : PrismApplication
{
    protected override Window CreateShell() =>
        Container.Resolve<ShellWindow>();

    protected override void RegisterTypes(IContainerRegistry container)
    {
        container.RegisterSingleton<ITaskRepository, ApiTaskRepository>();
        container.RegisterForNavigation<TaskListView, TaskListViewModel>();
    }

    protected override void OnInitialized()
    {
        base.OnInitialized();
        var regionManager = Container.Resolve<IRegionManager>();
        regionManager.RequestNavigate("ContentRegion", nameof(TaskListView));
    }

    protected override void ConfigureModuleCatalog(IModuleCatalog moduleCatalog)
    {
        // один модуль — можно опустить IModule и держать всё в App
    }
}
