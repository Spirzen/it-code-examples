type User struct {
    Email    string `json:"email" validate:"required,email"`
    Password string `json:"password" validate:"required,min=8"`
}

app.Post("/register", func(c *fiber.Ctx) error {
    var u User
    if err := c.BodyParser(&u); err != nil {
        return c.Status(400).JSON(fiber.Map{"error": "invalid JSON"})
    }
    if err := validate.Struct(u); err != nil {
        return c.Status(400).JSON(fiber.Map{"error": err.Error()})
    }
    // ...
})
