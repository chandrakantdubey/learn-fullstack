from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import get_db
from .models import Task
from .schemas import TaskCreate, TaskRead

router = APIRouter(prefix="/v1/tasks", tags=["tasks"])

# Temporary identity boundary for the first vertical slice.
# Replace with the real authenticated principal once auth is implemented.
SYSTEM_OWNER_ID = UUID("00000000-0000-0000-0000-000000000001")


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)) -> Task:
    task = Task(owner_id=SYSTEM_OWNER_ID, title=payload.title, description=payload.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)) -> list[Task]:
    stmt = select(Task).where(Task.owner_id == SYSTEM_OWNER_ID).order_by(Task.created_at.desc())
    return list(db.scalars(stmt).all())
