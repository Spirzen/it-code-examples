type Logger struct{}

func (l Logger) Log(msg string) {
    fmt.Println("[LOG]", msg)
}

type Service struct {
    Logger // встраивание
    name   string
}

func (s Service) Run() {
    s.Log("Starting service: " + s.name) // вызов метода встроенного типа
}
