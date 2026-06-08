// Быстрое копирование без аллокаций
unsafe
{
    byte* src = ...;
    byte* dst = ...;
    Unsafe.CopyBlock(dst, src, (uint)1024);
}

// Чтение int из байтового буфера без выравнивания
ReadOnlySpan<byte> data = ...;
int value = Unsafe.ReadUnaligned<int>(ref MemoryMarshal.GetReference(data));

// Обход ограничений generic-параметров
T CreateDefault<T>() => Unsafe.As<byte, T>(ref Unsafe.AsRef<byte>(null));
// (осторожно: может нарушить безопасность — только для value types с default layout)
