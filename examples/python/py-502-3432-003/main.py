from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth import (
    FAKE_USER,
    create_access_token,
    get_current_user,
    verify_password,
)


@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != FAKE_USER["username"] or not verify_password(
        form.password, FAKE_USER["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": create_access_token(form.username), "token_type": "bearer"}


@app.get("/notes", response_model=list[NoteOut])
def list_notes(_user: str = Depends(get_current_user)):
    return [NoteOut(**n) for n in _notes.values()]
