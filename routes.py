from fastapi import APIRouter, HTTPException
from models import Task
from database import todo_list

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return todo_list

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    if 0 <= task_id < len(todo_list):
        return todo_list[task_id]
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/tasks")
def create_task(task: Task):
    todo_list.append(task)
    return {"message": "Task created", "task": task}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id] = task
        return {"message": "Task updated", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(todo_list):
        deleted = todo_list.pop(task_id)
        return {"message": "Task deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")

@router.patch("/tasks/{task_id}/toggle")
def toggle_task_done(task_id: int):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id].done = not todo_list[task_id].done
        return {"message": "Task status toggled", "task": todo_list[task_id]}
    raise HTTPException(status_code=404, detail="Task not found")
