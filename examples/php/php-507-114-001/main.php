function foo(string $answer): void
{
    switch ($answer) {
        case 'no':
            echo 'You answered with No';
            break;
        case 'yes':
            echo 'You answered with Yes';
            break;
        default:
            // Not supposed to end up here.
            throw new LogicException('Unexpected answer ' . $answer);
    }
}
