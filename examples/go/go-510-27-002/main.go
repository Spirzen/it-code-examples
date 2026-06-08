socketPath := "/tmp/myapp.sock"
_ = os.Remove(socketPath) // старый файл сокета

ln, err := net.Listen("unix", socketPath)
if err != nil {
    log.Fatal(err)
}
defer ln.Close()
defer os.Remove(socketPath)

for {
    conn, err := ln.Accept()
    if err != nil {
        continue
    }
    go handleConn(conn)
}
