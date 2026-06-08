function toMessage(error: unknown): string {
  if (error instanceof Error) return error.message;
  if (typeof error === "string") return error;
  return "Неизвестная ошибка";
}

async function safeLoad(id: string): Promise<User | null> {
  try {
    return await loadUser(id);
  } catch (error: unknown) {
    console.error(toMessage(error));
    return null;
  }
}
