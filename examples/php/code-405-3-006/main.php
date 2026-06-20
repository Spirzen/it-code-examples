<?php
/**
 * Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
 *
 * Для учебного сравнения без сети используем usleep.
 * Блок curl_multi показывает реальный API для параллельных исходящих запросов.
 */

declare(strict_types=1);

$urls = [
    ['https://example.com/page1', 2_000_000], // мкс
    ['https://example.com/page2', 3_500_000],
    ['https://example.com/page3', 1_500_000],
    ['https://example.com/page4', 2_500_000],
    ['https://example.com/page5', 1_000_000],
];

function downloadSequential(array $urls): float
{
    echo "\n1. ПОСЛЕДОВАТЕЛЬНО (usleep в цикле)\n";
    $start = microtime(true);
    foreach ($urls as [$url, $delayUs]) {
        usleep($delayUs);
        echo "  Готово: {$url}\n";
    }
    $elapsed = microtime(true) - $start;
    printf("  Время: %.2f с\n", $elapsed);
    return $elapsed;
}

function downloadCurlMultiSimulated(array $urls): float
{
    echo "\n2. ПАРАЛЛЕЛЬНО (curl_multi — структура API)\n";
    $start = microtime(true);

    $mh = curl_multi_init();
    $handles = [];

    foreach ($urls as [$url, $delayUs]) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT_MS => (int) ($delayUs / 1000) + 500,
            CURLOPT_NOSIGNAL => true,
        ]);
        curl_multi_add_handle($mh, $ch);
        $handles[] = ['ch' => $ch, 'url' => $url, 'delayUs' => $delayUs];
    }

    // Если сеть недоступна — имитируем параллельное ожидание локально
    $running = null;
    do {
        $status = curl_multi_exec($mh, $running);
        if ($running > 0) {
            curl_multi_select($mh, 0.05);
        }
        if ($status !== CURLM_OK) {
            break;
        }
    } while ($running > 0);

    foreach ($handles as $item) {
        $body = curl_multi_getcontent($item['ch']);
        if ($body === false || $body === '') {
            usleep($item['delayUs']);
        }
        echo "  Готово: {$item['url']}\n";
        curl_multi_remove_handle($mh, $item['ch']);
        curl_close($item['ch']);
    }

    curl_multi_close($mh);

    $elapsed = microtime(true) - $start;
    printf("  Время: %.2f с\n", $elapsed);
    return $elapsed;
}

echo "=== PHP — sequential vs curl_multi ===\n";

$seq = downloadSequential($urls);
$par = downloadCurlMultiSimulated($urls);

echo "\n--- Итог ---\n";
printf("Последовательно: %.2f с\n", $seq);
printf("curl_multi:      %.2f с\n", $par);
printf("Ускорение:       %.2fx\n", $seq / max($par, 0.001));
