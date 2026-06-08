[HttpPost]
public async Task<IActionResult> Login(string returnUrl)
{
    var claims = new[]
    {
        new Claim(ClaimTypes.Name, "Timur"),
        new Claim(ClaimTypes.Role, "Admin")
    };
    var identity = new ClaimsIdentity(claims, "Cookies");
    var principal = new ClaimsPrincipal(identity);
    var props = new AuthenticationProperties { IsPersistent = true };

    await HttpContext.SignInAsync("Cookies", principal, props);
    return LocalRedirect(returnUrl ?? "/");
}
