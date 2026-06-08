public class MinimumAgeHandler : AuthorizationHandler<MinimumAgeRequirement>
{
    protected override Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        MinimumAgeRequirement requirement)
    {
        var dateOfBirthClaim = context.User.FindFirst(ClaimTypes.DateOfBirth);
        if (dateOfBirthClaim is null) return Task.CompletedTask;

        if (DateTime.Parse(dateOfBirthClaim.Value).AddYears(requirement.MinimumAge) <= DateTime.Today)
            context.Succeed(requirement);

        return Task.CompletedTask;
    }
}
