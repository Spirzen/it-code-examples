package main

import (

	"crypto/rand"
	"fmt"
	"math/big"
)

func generatePassword(length int) string {
	const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
	if length <= 0 {
		return ""
	}

	password := make([]byte, length)
	for i := range password {
		// Получаем случайное число в диапазоне [0, len(charset))
		num, err := rand.Int(rand.Reader, big.NewInt(int64(len(charset))))
		if err != nil {
			panic(err)
		}
		password[i] = charset[num.Int64()]
	}
	
	return string(password)
}

func main() {
	pass := generatePassword(16)
	fmt.Println("Сгенерированный пароль:", pass)
}
