func main() {
	v := NewVerifier(15 * time.Second)
	printResult(v.Verify("user@gmail.com"))
}

func printResult(r Result) {
	fmt.Printf("Email:  %s\n", r.Email)
	fmt.Printf("Формат: %s\n", yesNo(r.Valid))
	if r.Domain != "" {
		fmt.Printf("Domain: %s\n", r.Domain)
	}
	if r.MXHost != "" {
		fmt.Printf("MX:     %s\n", r.MXHost)
	}
	switch {
	case r.Exists == nil:
		fmt.Printf("SMTP:   не проверен (%s)\n", r.Detail)
	case *r.Exists:
		fmt.Printf("SMTP:   вероятно существует (%s)\n", r.Detail)
	default:
		fmt.Printf("SMTP:   не существует (%s)\n", r.Detail)
	}
	if r.Error != nil {
		fmt.Printf("Ошибка: %v\n", r.Error)
	}
}

func yesNo(v bool) string {
	if v {
		return "корректный"
	}
	return "некорректный"
}
