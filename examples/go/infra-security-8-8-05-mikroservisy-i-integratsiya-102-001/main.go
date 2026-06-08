func handler(w http.ResponseWriter, r *http.Request) {
    id := r.URL.Query().Get("id")

    body, err := io.ReadAll(r.Body)
    if err != nil {
        http.Error(w, "bad request", http.StatusBadRequest)
        return
    }
    defer r.Body.Close()

    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(map[string]string{
        "id":   id,
        "body": string(body),
    })
}
