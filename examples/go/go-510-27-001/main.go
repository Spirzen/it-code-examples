func main() {
    ln, err := net.Listen("tcp", ":9000")
    if err != nil {
        log.Fatal(err)
    }
    defer ln.Close()

    for {
        conn, err := ln.Accept()
        if err != nil {
            log.Print(err)
            continue
        }
        go handleConn(conn) // одна горутина на соединение
    }
}

func handleConn(c net.Conn) {
    defer c.Close()
    io.Copy(c, c) // эхо: всё прочитанное — обратно клиенту
}
