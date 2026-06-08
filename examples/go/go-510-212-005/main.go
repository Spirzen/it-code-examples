// ParseDomain извлекает домен из email или возвращает строку как есть.
func ParseDomain(input string) (string, error) {
	input = strings.TrimSpace(input)
	if strings.Contains(input, "@") {
		parts := strings.SplitN(input, "@", 2)
		if len(parts[1]) == 0 {
			return "", fmt.Errorf("домен не указан")
		}
		return parts[1], nil
	}
	if net.ParseIP(input) != nil {
		return "", fmt.Errorf("ожидается домен или email, не IP")
	}
	return input, nil
}
