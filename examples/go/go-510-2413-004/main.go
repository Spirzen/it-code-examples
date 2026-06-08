e.HTTPErrorHandler = func(err error, c echo.Context) {
    code := http.StatusInternalServerError
    msg := "internal error"

    var he *echo.HTTPError
    if errors.As(err, &he) {
        code = he.Code
        msg = fmt.Sprint(he.Message)
    }

    _ = c.JSON(code, map[string]any{
        "error": map[string]string{
            "message": msg,
        },
    })
}
