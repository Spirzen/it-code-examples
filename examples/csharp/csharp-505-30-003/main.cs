// Сгенерированный класс <>d__0 (имя условное)
class IteratorStateMachine : IEnumerator<int>
{
    private int _state;      // «где мы остановились»
    private int _current;    // значение для свойства Current
    // параметры и локальные переменные исходного метода — тоже поля

    public int Current => _current;

    public bool MoveNext()
    {
        switch (_state)
        {
            case -1: _state = 0; goto case 0; // первый MoveNext: вход в метод
            case 0:  _state = 1; _current = 1; return true;
            case 1:  _state = 2; _current = 2; return true;
            case 2:  _state = -2; _current = 3; return true; // -2 = завершено
            default: return false;
        }
    }
}
