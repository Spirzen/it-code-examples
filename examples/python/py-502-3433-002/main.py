from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/users", response_model=UserRead, status_code=201)
def create_user(body: UserCreate, db: Session = Depends(get_db)):
    if db.query(UserRow).filter_by(username=body.username).first():
        raise HTTPException(status_code=409, detail="username занят")
    row = UserRow(username=body.username, email=body.email)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    row = db.get(UserRow, user_id)
    if row is None:
        raise HTTPException(status_code=404, detail="не найден")
    return row
