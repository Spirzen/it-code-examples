import { Router } from 'express';

export function createNotesRouter(store) {
  const router = Router();

  router.get('/', (_req, res) => {
    res.json(store.list());
  });

  router.post('/', (req, res) => {
    const text = String(req.body?.text ?? '').trim();
    if (!text) return res.status(400).json({ error: 'text is required' });
    res.status(201).json(store.add(text));
  });

  router.delete('/:id', (req, res) => {
    const ok = store.remove(Number(req.params.id));
    if (!ok) return res.status(404).json({ error: 'not found' });
    res.status(204).send();
  });

  return router;
}
