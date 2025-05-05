from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.models import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def get_todos(db: Session, user_id: int) -> List[Todo]:
    """Retrieve all todos for a given user."""
    return db.query(Todo).filter(Todo.owner_id == user_id).all()


def get_todo(db: Session, todo_id: int, user_id: int) -> Optional[Todo]:
    """Retrieve a specific todo by ID and user."""
    return db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user_id).first()


def create_todo(db: Session, todo: TodoCreate, user_id: int) -> Todo:
    """Create a new todo for the specified user."""
    db_todo = Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, db_todo: Todo, updates: TodoUpdate) -> Todo:
    """Update an existing todo with new data."""
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, db_todo: Todo) -> None:
    """Delete the specified todo."""
    db.delete(db_todo)
    db.commit()