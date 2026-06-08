abstract class Importer
{
    public function import($file)
    {
        $this->connect();
        $data = $this->parse($file);
        $this->validate($data);
        $this->store($data);
        $this->disconnect();
    }

    protected function connect() { /* Подключение */ }
    protected function parse($file) { /* Абстрактный метод */ }
    protected function validate($data) { /* Проверка */ }
    protected function store($data) { /* Абстрактный метод */ }
    protected function disconnect() { /* Отключение */ }
}
