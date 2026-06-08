<?php
declare(strict_types=1);

function parsePagination(array $query): array
{
    $page = filter_var($query["page"] ?? 1, FILTER_VALIDATE_INT);
    $limit = filter_var($query["limit"] ?? 20, FILTER_VALIDATE_INT);

    if ($page === false || $page < 1) {
        $page = 1;
    }
    if ($limit === false || $limit < 1 || $limit > 100) {
        $limit = 20;
    }

    return ["page" => $page, "limit" => $limit];
}
