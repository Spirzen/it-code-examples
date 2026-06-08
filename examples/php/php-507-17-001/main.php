declare(strict_types=1);

/**
 * @throws \InvalidArgumentException
 */
function normalizeEmail(string $rawEmail): string
{
    $email = mb_strtolower(trim($rawEmail));

    if ($email === '') {
        throw new \InvalidArgumentException("Email is required");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new \InvalidArgumentException("Email format is invalid");
    }

    return $email;
}
