type hub struct {
    clients map[*websocket.Conn]struct{}
    broadcast chan []byte
    register  chan *websocket.Conn
    unregister chan *websocket.Conn
}

func (h *hub) run() {
    for {
        select {
        case c := <-h.register:
            h.clients[c] = struct{}{}
        case c := <-h.unregister:
            delete(h.clients, c)
            c.Close()
        case msg := <-h.broadcast:
            for c := range h.clients {
                if err := c.WriteMessage(websocket.TextMessage, msg); err != nil {
                    delete(h.clients, c)
                    c.Close()
                }
            }
        }
    }
}
