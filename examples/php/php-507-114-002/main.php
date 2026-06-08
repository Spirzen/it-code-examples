// Вместо этого:
if ($member->hidesBaseClassMember && ($member->nodeType != NodeType::INSTANCE_INITIALIZER)) {
    // что-то делаем
}

// Делайте так:
if ($this->nonConstructorMemberUsesNewKeyword($member)) {
    // что-то делаем
}

private function nonConstructorMemberUsesNewKeyword(Member $member): bool
{
    return $member->hidesBaseClassMember && ($member->nodeType != NodeType::INSTANCE_INITIALIZER);
}
