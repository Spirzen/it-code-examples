package main

import (

	"encoding/json"
	"fmt"
	"os"
)

const dataFile = "tasks.json"

func loadTasks() (*TaskList, error) {
	data, err := os.ReadFile(dataFile)
	if err != nil {
		if os.IsNotExist(err) {
			return &TaskList{Tasks: []Task{}}, nil
		}
		return nil, err
	}

	var list TaskList
	if err := json.Unmarshal(data, &list); err != nil {
		return nil, err
	}
	return &list, nil
}

func saveTasks(list *TaskList) error {
	data, err := json.MarshalIndent(list, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(dataFile, data, 0644)
}

func addTask(list *TaskList, title string, priority int) {
	newID := 1
	if len(list.Tasks) > 0 {
		newID = list.Tasks[len(list.Tasks)-1].ID + 1
	}
	list.Tasks = append(list.Tasks, Task{
		ID:       newID,
		Title:    title,
		Done:     false,
		Priority: priority,
	})
}

func main() {
	list, err := loadTasks()
	if err != nil {
		fmt.Println("Ошибка загрузки:", err)
		os.Exit(1)
	}

	addTask(list, "Изучить Go", 1)
	addTask(list, "Написать статью", 2)

	if err := saveTasks(list); err != nil {
		fmt.Println("Ошибка сохранения:", err)
		os.Exit(1)
	}

	fmt.Println("Задачи сохранены в tasks.json")
	
	// Вывод для проверки
	jsonOut, _ := json.MarshalIndent(list, "", "  ")
	fmt.Println(string(jsonOut))
}
