<?php
$status = 404;

switch ($status) {
    case 200:
        echo "OK";
        break;
    case 404:
        echo "Страница не найдена";
        break;
    case 500:
        echo "Ошибка сервера";
        break;
    default:
        echo "Неизвестный статус";
}
