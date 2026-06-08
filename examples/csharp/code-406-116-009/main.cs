public class EventLeakExample
{
    private static readonly List<DataProcessor> _processors = new();
    
    public void RegisterProcessor(DataProcessor processor)
    {
        // Подписка на событие без сохранения ссылки для отписки
        processor.DataReady += HandleData;
        _processors.Add(processor); // Удержание процессора в памяти
    }
    
    private void HandleData(object sender, DataEventArgs e)
    {
        // Обработка данных
    }
    
    // Отписка никогда не происходит — процессоры накапливаются
}
