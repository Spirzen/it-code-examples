
import { z } from 'zod';

const createNoteSchema = z.object({
  text: z.string().trim().min(1).max(2000),
});

router.post('/', (req, res, next) => {
  const parsed = createNoteSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { text } = parsed.data; // уже обрезанная и проверенная строка
  // store.add(text) ...
});
