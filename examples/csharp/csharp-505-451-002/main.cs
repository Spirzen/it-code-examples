builder.Services.Configure<RouteOptions>(options =>
{
    options.ConstraintMap.Add("slug", typeof(SlugConstraint));
});

public class SlugConstraint : IRouteConstraint
{
    public bool Match(HttpContext httpContext, IRouter route, string routeKey, 
                       RouteValueDictionary values, RouteDirection routeDirection)
    {
        var value = values[routeKey]?.ToString();
        return value != null && Regex.IsMatch(value, @"^[a-z0-9\-]+$");
    }
}
