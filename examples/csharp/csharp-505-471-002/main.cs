// Из массива
var arr = new byte[1024];
Span<byte> span = arr.AsSpan();
ReadOnlySpan<byte> roSpan = arr.AsSpan().Slice(10, 100);

// Из строки
ReadOnlySpan<char> strSpan = "Hello".AsSpan();

// Из неуправляемой памяти
unsafe
{
    void* ptr = NativeMemory.Alloc(1024);
    Span<byte> span = new(ptr, 1024);
    NativeMemory.Free(ptr); // ← осторожно: span живёт дольше памяти!
}

// Из stackalloc (без unsafe в C# 7.2+)
Span<byte> buffer = stackalloc byte[256];

// Из Memory<T>
Memory<byte> mem = new byte[1024];
Span<byte> span = mem.Span; // только в синхронном контексте!
