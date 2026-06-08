public class SortContext
{
    public void ExecuteSort(List<int> list, Action<List<int>> sortAlgorithm)
    {
        sortAlgorithm(list);
    }
}

var context = new SortContext();

context.ExecuteSort(numbers, list => list.Sort());
context.ExecuteSort(numbers, list =>
{
    // своя логика сортировки
});
