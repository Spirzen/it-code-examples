
import (

    "fmt"
    "runtime"
)

func main() {
    fmt.Printf("Количество горутин: %d\n", runtime.NumGoroutine())
    
    buf := make([]byte, 65536)
    n := runtime.Stack(buf, true)
    fmt.Printf("%s\n", buf[:n])
}
