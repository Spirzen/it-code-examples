builder.Services.AddQuartz(q =>
{
    q.UseMicrosoftDependencyInjectionJobFactory();

    // Job и Trigger
    var jobKey = new JobKey("backup");
    q.AddJob<BackupJob>(jobKey, j => j.WithDescription("Nightly backup"));

    q.AddTrigger(t => t
        .ForJob(jobKey)
        .WithIdentity("backup-trigger")
        .WithCronSchedule("0 0 2 * * ?") // ежедневно в 02:00 UTC
        .WithDescription("Triggers backup every day at 2 AM"));
});

builder.Services.AddQuartzHostedService(options =>
{
    options.WaitForJobsToComplete = true;
});
