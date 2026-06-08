<?php
declare(strict_types=1);

function normalizeStatus(int $code): string
{
    return match ($code) {
        200, 201 => "ok",
        400 => "bad_request",
        404 => "not_found",
        default => "unknown",
    };
}

echo normalizeStatus(404);
