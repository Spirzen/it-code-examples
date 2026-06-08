
import { z } from "zod";

const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
});

try {
  const raw_data = '{"id": 1, "name": "Алиса"}';
  const parsed_data = JSON.parse(raw_data);
  const user = UserSchema.parse(parsed_data);
  console.log(user.name);
} catch (error) {
  console.error("Сбой парсинга или валидации:", error);
}
