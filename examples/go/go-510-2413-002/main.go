func listNotes(c echo.Context) error {
    mu.Lock()
    defer mu.Unlock()
    return c.JSON(http.StatusOK, notes)
}

func createNote(c echo.Context) error {
    var body NoteCreate
    if err := c.Bind(&body); err != nil {
        return echo.NewHTTPError(http.StatusBadRequest, err.Error())
    }
    mu.Lock()
    note := Note{ID: nextID, Text: body.Text}
    nextID++
    notes = append(notes, note)
    mu.Unlock()
    return c.JSON(http.StatusCreated, note)
}

func deleteNote(c echo.Context) error {
    id, err := strconv.Atoi(c.Param("id"))
    if err != nil {
        return echo.NewHTTPError(http.StatusBadRequest, "invalid id")
    }
    mu.Lock()
    defer mu.Unlock()
    for i, n := range notes {
        if n.ID == id {
            notes = append(notes[:i], notes[i+1:]...)
            return c.NoContent(http.StatusNoContent)
        }
    }
    return echo.NewHTTPError(http.StatusNotFound, "not found")
}
