<?php
declare(strict_types=1);

final class Input
{
    public static function intFromGet(string $key, int $default = 0): int
    {
        $value = filter_input(INPUT_GET, $key, FILTER_VALIDATE_INT);
        return $value === false || $value === null ? $default : $value;
    }

    public static function stringFromPost(string $key, string $default = ""): string
    {
        $value = filter_input(INPUT_POST, $key, FILTER_UNSAFE_RAW);
        return $value === null ? $default : trim((string)$value);
    }
}
