public class AccountController : Controller
{
    private readonly IStringLocalizer<AccountController> _localizer;
    public AccountController(IStringLocalizer<AccountController> localizer) => _localizer = localizer;

    public IActionResult Login()
    {
        // Простая строка
        ViewData["Message"] = _localizer["WelcomeMessage"];

        // С параметрами (форматирование по порядку)
        var greeting = _localizer["WelcomeMessage", User.Identity.Name];

        // Проверка существования
        if (_localizer["NotFoundKey"].ResourceNotFound)
            throw new InvalidOperationException("Missing translation");

        return View();
    }

    public IActionResult Error()
    {
        // Безопасное значение по умолчанию
        var msg = _localizer.GetString("UnknownError", "An unknown error occurred");
        return Content(msg);
    }
}
