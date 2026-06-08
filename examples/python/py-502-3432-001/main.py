from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API", version="0.1.0")

_notes: dict[int, dict] = {}
_next_id = 1


class NoteCreate(BaseModel):
    text: str = Field(min_length=1, max_length=500)


class NoteOut(BaseModel):
    id: int
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notes", response_model=list[NoteOut])
def list_notes():
    return [NoteOut(**n) for n in _notes.values()]


@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(body: NoteCreate):
    global _next_id
    note = {"id": _next_id, "text": body.text}
    _notes[_next_id] = note
    _next_id += 1
    return NoteOut(**note)


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int = Path(ge=1)):
    if note_id not in _notes:
        raise HTTPException(status_code=404, detail="note not found")
    del _notes[note_id]
