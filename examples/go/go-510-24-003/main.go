// ... импорты ...

func main() {
	fmt.Print("Введите ваше имя: ")
	reader := bufio.NewReader(os.Stdin)
	name, err := reader.ReadString('\n')
	if err != nil {
		fmt.Fprintf(os.Stderr, "Ошибка ввода: %v\n", err)
		os.Exit(1)
	}
	name = name[:len(name)-1]

	greeting := buildGreeting(name)
	fmt.Println(greeting)
}

func buildGreeting(name string) string {
	return "Hello, " + name + "!"
}
