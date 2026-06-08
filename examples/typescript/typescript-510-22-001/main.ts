// types/dto.ts — контракт HTTP
export type CreateUserDto = {
  email: string;
  name: string;
};

// domain/user.ts — бизнес-сущность
export type User = {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
};

// mappers
export function fromDto(dto: CreateUserDto): Omit<User, "id" | "createdAt"> {
  return { email: dto.email.trim(), name: dto.name.trim() };
}
