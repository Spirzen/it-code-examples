// Плохо
if (member.HidesBaseClassMember && (member.NodeType != NodeType.InstanceInitializer))
{
    // обработка
}

// Хорошо
if (NonConstructorMemberUsesNewKeyword(member))
{
    // обработка
}

private bool NonConstructorMemberUsesNewKeyword(Member member)
{
    return member.HidesBaseClassMember && 
           (member.NodeType != NodeType.InstanceInitializer);
}
