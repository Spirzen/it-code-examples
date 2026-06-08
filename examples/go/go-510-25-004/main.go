func createUser(w http.ResponseWriter, r *http.Request) {
    var body struct {
        Name string `json:"name"`
    }
    if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
        http.Error(w, "invalid json", http.StatusBadRequest)
        return
    }
    if strings.TrimSpace(body.Name) == "" {
        http.Error(w, "name is required", http.StatusBadRequest)
        return
    }
    writeJSON(w, http.StatusCreated, body)
}
