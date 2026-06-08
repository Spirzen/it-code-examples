type Flusher interface {
    Flush() error
}

func sendResponse(w io.Writer, data []byte) error {
    _, err := w.Write(data)
    if err != nil {
        return err
    }

    if f, ok := w.(Flusher); ok {
        return f.Flush()
    }
    return nil
}
