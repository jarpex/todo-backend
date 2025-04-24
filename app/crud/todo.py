from sqlalchemy.orm import Session
from app.db.models import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from typing import List, Optional

def get_todos(db: Session, user_id: int) -> List[Todo]:
    return db.query(Todo).filter(Todo.owner_id == user_id).all()

def get_todo(db: Session, todo_id: int, user_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user_id).first()

def create_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, db_todo: Todo, updates: TodoUpdate):
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, db_todo: Todo):
    db.delete(db_todo)
    db.commit()