public interface ICommand
{
    void Execute();
    void Undo();
}

public class SaveDocumentCommand : ICommand
{
    private readonly DocumentService _receiver;
    private readonly string _path;

    public SaveDocumentCommand(DocumentService receiver, string path)
    {
        _receiver = receiver;
        _path = path;
    }

    public void Execute() => _receiver.Save(_path);
    public void Undo() => _receiver.RestorePreviousVersion(_path);
}
