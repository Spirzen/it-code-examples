class User {
    private string name;

    public string Name { // Свойство
        get { return name; }
        set {
            if (!string.IsNullOrEmpty(value)) {
                name = value;
            } else {
                throw new Exception("Имя не может быть пустым!");
            }
        }
    }
}
