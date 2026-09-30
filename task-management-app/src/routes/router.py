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


@task_routes.get("/all_task/{task_id}")
def get_one_task(task_id:int,db= Depends(get_db)):
    return tasksController.get_one_task(task_id,db)


@task_routes.put("/all_task/{task_id}")
def update_task(task_id:int,body:CreateTaskDTO,db = Depends(get_db)):
    return tasksController.update_task(body,task_id,db)