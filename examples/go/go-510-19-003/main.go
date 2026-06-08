app := fiber.New()
// ... routes

ln, err := net.Listen("tcp", ":3000")
if err != nil { /* handle */ }

go func() {
    if err := app.Listener(ln); err != nil {
        log.Println("Server error:", err)
    }
}()

// ... wait for signal

if err := app.Shutdown(); err != nil {
    log.Println("Shutdown error:", err)
}
