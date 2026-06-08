class User {
    private string name;

    public string getName() { // Геттер
        return name;
    }

    public void setName(string newName) { // Сеттер
        if (!string.IsNullOrEmpty(newName)) {
            name = newName;
        } else {
            throw new Exception("Имя не может быть пустым!");
        }
    }
}

