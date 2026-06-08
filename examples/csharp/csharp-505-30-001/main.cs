public class TreeNode
{
    public int Value { get; set; }
    public List<TreeNode> Children { get; } = new();

    public IEnumerable<int> TraverseDepthFirst()
    {
        yield return Value;
        foreach (var child in Children)
        {
            foreach (var value in child.TraverseDepthFirst())
            {
                yield return value;
            }
        }
    }
}
