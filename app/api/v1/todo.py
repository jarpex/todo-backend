from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate
from app.crud.todo import get_todos, get_todo, create_todo, update_todo, delete_todo
from app.api.deps import get_current_user
from app.db.models import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TodoOut])
def read_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_todos(db, user_id=current_user.id)

@router.post("/", response_model=TodoOut)
def create_new_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_todo(db, todo, user_id=current_user.id)

@router.put("/{todo_id}", response_model=TodoOut)
def update_existing_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = get_todo(db, todo_id, current_user.id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return update_todo(db, db_todo, todo)

@router.delete("/{todo_id}", status_code=204)
def delete_existing_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = get_todo(db, todo_id, current_user.id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    delete_todo(db, db_todo)