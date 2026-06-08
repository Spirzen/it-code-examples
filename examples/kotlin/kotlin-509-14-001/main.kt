class BitIterator(private var value: Int) : Iterator<Boolean> {
    private var bitIndex = 0
    override fun hasNext() = bitIndex < 32
    override fun next(): Boolean {
        if (!hasNext()) throw NoSuchElementException()
        return (value shr bitIndex++ and 1) == 1
    }
}

operator fun Int.iterator() = BitIterator(this)

// Использование:
for (bit in 5) {  // 5 = 101₂
    print(if (bit) '1' else '0')
}
// Выведет: 10100000000000000000000000000000
