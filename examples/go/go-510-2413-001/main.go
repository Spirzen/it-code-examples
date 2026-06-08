package main

import (

    "net/http"
    "strconv"
    "sync"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

type Note struct {
    ID   int    `json:"id"`
    Text string `json:"text"`
}

type NoteCreate struct {
    Text string `json:"text" validate:"required,min=1,max=500"`
}

var (
    notes  []Note
    nextID = 1
    mu     sync.Mutex
)

func main() {
    e := echo.New()
    e.Use(middleware.Logger())
    e.Use(middleware.Recover())

    e.GET("/health", func(c echo.Context) error {
        return c.JSON(http.StatusOK, map[string]string{"status": "ok"})
    })

    g := e.Group("/api")
    g.GET("/notes", listNotes)
    g.POST("/notes", createNote)
    g.DELETE("/notes/:id", deleteNote)

    e.Logger.Fatal(e.Start(":8080"))
}
