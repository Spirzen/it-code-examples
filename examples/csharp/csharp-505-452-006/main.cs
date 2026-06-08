builder.Services.AddAuthentication(options =>
{
    options.DefaultScheme = "Cookies";              // для MVC
    options.DefaultChallengeScheme = "oidc";       // для входа через Google
    options.DefaultAuthenticateScheme = "Cookies";  // кто устанавливает User
})
.AddCookie("Cookies", options =>
{
    options.LoginPath = "/account/login";
    options.AccessDeniedPath = "/account/access-denied";
    options.ExpireTimeSpan = TimeSpan.FromDays(14);
    options.SlidingExpiration = true;
})
.AddJwtBearer("Bearer", options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidIssuer = "https://myapp.com",
        ValidateAudience = true,
        ValidAudience = "api",
        ValidateLifetime = true,
        ClockSkew = TimeSpan.FromMinutes(5),
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("very-long-secret-key"))
    };
});
