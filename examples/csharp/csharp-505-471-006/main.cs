[Generator]
public partial class MyGenerator : IIncrementalGenerator
{
    public void Initialize(IncrementalGeneratorInitializationContext context)
    {
        var provider = context.SyntaxProvider
            .CreateSyntaxProvider(
                predicate: static (s, _) => s is ClassDeclarationSyntax c && c.AttributeLists.Count > 0,
                transform: static (ctx, _) => (ClassDeclarationSyntax)ctx.Node)
            .Collect();

        context.RegisterSourceOutput(provider, (spc, classes) =>
        {
            foreach (var c in classes)
                spc.AddSource($"{c.Identifier}.g.cs", $$"""
                    partial class {{c.Identifier}}
                    {
                        public void GeneratedMethod() => Console.WriteLine("Hello");
                    }
                    """);
        });
    }
}
