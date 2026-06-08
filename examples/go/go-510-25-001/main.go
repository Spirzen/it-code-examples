var page = template.Must(template.New("home").Parse(`
<!DOCTYPE html>
<html><body>
  <h1>{{.Title}}</h1>
  <p>Привет, {{.Name}}</p>
</body></html>
`))

func home(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    _ = page.Execute(w, struct {
        Title, Name string
    }{"Заметки", r.URL.Query().Get("name")})
}
