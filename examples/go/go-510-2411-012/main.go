package main

import (

	"fmt"
	"time"
)

func convertDate(dateString, layout, outputLayout string) error {
	loc, err := time.LoadLocation("UTC")
	if err != nil {
		return err
	}

	t, err := time.ParseInLocation(layout, dateString, loc)
	if err != nil {
		return fmt.Errorf("неверный формат входной даты: %w", err)
	}

	formatted := t.Format(outputLayout)
	fmt.Printf("Вход: %s (%s)\n", dateString, layout)
	fmt.Printf("Выход: %s (%s)\n", formatted, outputLayout)
	return nil
}

func main() {
	input := "2026-05-06"
	layout := "2006-01-02"
	output := "02 January 2006"

	convertDate(input, layout, output)
}
