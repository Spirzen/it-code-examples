func createNote(c *fiber.Ctx) error {
    var body NoteCreate
    if err := c.BodyParser(&body); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }
    if body.Text == "" {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "text required"})
    }
    mu.Lock()
    note := Note{ID: nextID, Text: body.Text}
    nextID++
    notes = append(notes, note)
    mu.Unlock()
    return c.Status(fiber.StatusCreated).JSON(note)
}
