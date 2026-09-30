from fastapi import APIRouter, Depends
from src.controllers import tasksController 
from src.dtos.taskDto import CreateTaskDTO
from src.config.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:CreateTaskDTO,db = Depends(get_db)):
    return tasksController.create_task(body,db)


@task_routes.get("/all_tasks")
def get_all_Tasks(db = Depends(get_db)):
    return tasksController.get_tasks(db)