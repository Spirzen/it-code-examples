package main

import "testing"

func TestGreeting(t *testing.T) {
	input := "Alice"
	want := "Hello, Alice!"

	// Для изоляции логики вынесем формирование приветствия в отдельную функцию
	got := buildGreeting(input)

	if got != want {
		t.Errorf("buildGreeting(%q) = %q, want %q", input, got, want)
	}
}

// Вспомогательная функция, которую будем тестировать
func buildGreeting(name string) string {
	return "Hello, " + name + "!"
}
