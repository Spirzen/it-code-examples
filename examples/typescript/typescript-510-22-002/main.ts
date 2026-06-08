type ServiceError = "validation" | "conflict";
type ServiceResult<T> =
  | { ok: true; value: T }
  | { ok: false; error: ServiceError };

export function createUser(
  input: CreateUserDto,
  existingEmails: Set<string>,
): ServiceResult<User> {
  if (!input.email.includes("@")) {
    return { ok: false, error: "validation" };
  }
  if (existingEmails.has(input.email)) {
    return { ok: false, error: "conflict" };
  }
  const user: User = {
    id: crypto.randomUUID(),
    ...fromDto(input),
    createdAt: new Date(),
  };
  return { ok: true, value: user };
}
