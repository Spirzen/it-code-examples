package main

import (

    "strconv"
    "sync"

    "github.com/gofiber/fiber/v2"
)

type Note struct {
    ID   int    `json:"id"`
    Text string `json:"text"`
}

type NoteCreate struct {
    Text string `json:"text"`
}

var (
    notes  []Note
    nextID = 1
    mu     sync.Mutex
)

func main() {
    app := fiber.New()

    app.Get("/health", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{"status": "ok"})
    })

    api := app.Group("/api")
    api.Get("/notes", listNotes)
    api.Post("/notes", createNote)
    api.Delete("/notes/:id", deleteNote)

    app.Listen(":3000")
}
