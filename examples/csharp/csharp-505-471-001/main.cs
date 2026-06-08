public class FileStreamWrapper : Stream, IDisposable
{
    private FileStream? _stream;
    private bool _disposed;

    protected virtual void Dispose(bool disposing)
    {
        if (!_disposed)
        {
            if (disposing)
            {
                // Освободить управляемые ресурсы
                _stream?.Dispose();
            }
            // Освободить неуправляемые (если есть напрямую — редко)
            _stream = null;
            _disposed = true;
        }
    }

    public void Dispose()
    {
        Dispose(disposing: true);
        GC.SuppressFinalize(this); // отменить финализацию
    }

    // Финализатор (только если есть неуправляемые ресурсы напрямую)
    ~FileStreamWrapper()
    {
        Dispose(disposing: false);
    }

    // IAsyncDisposable (для асинхронных ресурсов)
    public async ValueTask DisposeAsync()
    {
        if (_stream != null)
        {
            await _stream.DisposeAsync().ConfigureAwait(false);
            _stream = null;
        }
        _disposed = true;
        GC.SuppressFinalize(this);
    }
}
