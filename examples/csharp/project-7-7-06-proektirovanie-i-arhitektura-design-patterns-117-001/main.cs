public interface ISortStrategy
{
    void Sort(List<int> list);
}

public class BubbleSortStrategy : ISortStrategy
{
    public void Sort(List<int> list)
    {
        // пузырьковая сортировка
    }
}

public class QuickSortStrategy : ISortStrategy
{
    public void Sort(List<int> list)
    {
        // быстрая сортировка
    }
}

public class SortContext
{
    private ISortStrategy _strategy;

    public SortContext(ISortStrategy strategy) => _strategy = strategy;

    public void SetStrategy(ISortStrategy strategy) => _strategy = strategy;

    public void ExecuteSort(List<int> list) => _strategy.Sort(list);
}
