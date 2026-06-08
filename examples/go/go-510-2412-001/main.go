package main

import (

    "net/http"
    "strconv"
    "sync"

    "github.com/gin-gonic/gin"
)

type Note struct {
    ID   int    `json:"id"`
    Text string `json:"text" binding:"required,min=1,max=500"`
}

var (
    notes  []Note
    nextID = 1
    mu     sync.Mutex
)

func main() {
    r := gin.Default()

    r.GET("/health", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"status": "ok"})
    })

    api := r.Group("/api")
    {
        api.GET("/notes", listNotes)
        api.POST("/notes", createNote)
        api.DELETE("/notes/:id", deleteNote)
    }

    r.Run(":8080")
}
