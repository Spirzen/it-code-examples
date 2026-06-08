type UserDto = { id: string; name: string; created_at: string };
type User = { id: string; name: string; createdAt: Date };

function fromDto(dto: UserDto): User {
  return {
    id: dto.id,
    name: dto.name,
    createdAt: new Date(dto.created_at),
  };
}

function toDto(user: User): UserDto {
  return {
    id: user.id,
    name: user.name,
    created_at: user.createdAt.toISOString(),
  };
}
