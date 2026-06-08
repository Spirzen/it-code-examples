enum Status
{
    case Draft;
    case Published;
    case Archived;
}

function canEdit(Status $status): bool
{
    return match ($status) {
        Status::Draft => true,
        Status::Published, Status::Archived => false,
    };
}
