import { z } from "zod";

const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1),
});

type CreateUserDto = z.infer<typeof CreateUserSchema>;

function parseCreateUser(body: unknown): Result<CreateUserDto, string> {
  const parsed = CreateUserSchema.safeParse(body);
  return parsed.success
    ? { ok: true, value: parsed.data }
    : { ok: false, error: parsed.error.message };
}
