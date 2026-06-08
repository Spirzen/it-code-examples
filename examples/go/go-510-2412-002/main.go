
import (

    "context"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "time"
)

srv := &http.Server{Addr: ":8080", Handler: r}
go func() { _ = srv.ListenAndServe() }()

quit := make(chan os.Signal, 1)
signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
<-quit

ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
_ = srv.Shutdown(ctx)
