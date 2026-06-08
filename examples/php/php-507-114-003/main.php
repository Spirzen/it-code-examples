<?php
/**
 * Класс Program
 * основной класс программы
 * выводящий текст "Hello, World!"
 */
class Program
{
    /**
     * Метод main() является
     * входной точкой работы программы
     * @param array $args Аргумент метода main()
     */
    public static function main(array $args): void
    {
        echo "Hello, World!\n";
    }
}
?>
