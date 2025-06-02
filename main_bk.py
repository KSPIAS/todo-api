from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ฐานข้อมูลจำลอง
todo_list = []

# Model
class Task(BaseModel):
    title: str
    description: str
    done: bool = False

# 1. GET ทั้งหมด
@app.get("/tasks")
def get_tasks():
    return todo_list

# 2. GET ทีละชิ้น
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if 0 <= task_id < len(todo_list):
        return todo_list[task_id]
    raise HTTPException(status_code=404, detail="Task not found")

# 3. POST สร้างงานใหม่
@app.post("/tasks")
def create_task(task: Task):
    todo_list.append(task)
    return {"message": "Task created", "task": task}

# 4. PUT แก้ไข
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id] = task
        return {"message": "Task updated", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

# 5. DELETE ลบงาน
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     if 0 <= task_id < len(todo_list):
#         deleted = todo_list.pop(task_id)
#         return {"message": "Task deleted", "task": deleted}
#     raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/by-title/{title}")
def delete_task_by_title(title: str):
    for i, task in enumerate(todo_list):
        if task.title == title:
            deleted = todo_list.pop(i)
            return {"message": "Task deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/toggle")
def toggle_task_done(task_id: int):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id].done = not todo_list[task_id].done
        return {"message": "Task status toggled", "task": todo_list[task_id]}
    raise HTTPException(status_code=404, detail="Task not found")

