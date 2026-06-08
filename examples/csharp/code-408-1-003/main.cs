class Автомобиль {
    private string _model;  // Приватное поле
    private int _year;      // Приватное поле

    public string Model {   // Свойство для поля _model
        get { return _model; }
        set {
            if (value == "") {
                throw new Exception("Модель не может быть пустой!");
            }
            _model = value;
        }
    }

    public int Year {       // Свойство для поля _year
        get { return _year; }
        set {
            if (value < 1900) {
                throw new Exception("Год выпуска не может быть меньше 1900!");
            }
            _year = value;
        }
    }
}
