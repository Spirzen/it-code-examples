import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

const notes = [];
let nextId = 1;

app.get('/health', (_req, res) => {
  res.json({ status: 'ok' });
});

app.get('/notes', (_req, res) => {
  res.json(notes);
});

app.post('/notes', (req, res) => {
  const text = String(req.body?.text ?? '').trim();
  if (!text) {
    return res.status(400).json({ error: 'text is required' });
  }
  const note = { id: nextId++, text, createdAt: new Date().toISOString() };
  notes.push(note);
  res.status(201).json(note);
});

app.delete('/notes/:id', (req, res) => {
  const id = Number(req.params.id);
  const idx = notes.findIndex((n) => n.id === id);
  if (idx === -1) {
    return res.status(404).json({ error: 'not found' });
  }
  notes.splice(idx, 1);
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`API: http://127.0.0.1:${PORT}`);
});
