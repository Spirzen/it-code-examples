package main

import (
	"regexp"
	"strings"
	"time"
)

var emailRegex = regexp.MustCompile(`^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$`)

// Result — результат проверки одного адреса.
type Result struct {
	Email  string
	Valid  bool   // синтаксис корректен
	Exists *bool  // nil — не удалось проверить через SMTP
	Domain string
	MXHost string
	Detail string
	Error  error
}

// Verifier проверяет email через DNS (MX) и SMTP (RCPT TO).
type Verifier struct {
	Timeout time.Duration
}

func NewVerifier(timeout time.Duration) *Verifier {
	return &Verifier{Timeout: timeout}
}

func (v *Verifier) Verify(email string) Result {
	email = strings.TrimSpace(strings.ToLower(email))
	result := Result{Email: email}

	if !emailRegex.MatchString(email) {
		result.Detail = "некорректный формат email"
		return result
	}
	result.Valid = true

	parts := strings.SplitN(email, "@", 2)
	result.Domain = parts[1]
	result.Detail = "синтаксис OK (DNS/SMTP — на следующих этапах)"
	return result
}
