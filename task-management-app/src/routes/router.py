from fastapi import APIRouter, Depends,status
from typing import List
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.controllers import tasksController 
from src.dtos.taskDto import CreateTaskDTO,TaskResponseTitleDto

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

@task_routes.delete("/all_task/{task_id}")
def delete_task(task_id:int,db= Depends(get_db)):
    return tasksController.delete_task(task_id,db)


# status_code will be send on successfull return code 
@task_routes.get("/best-practice/status-code",status_code=status.HTTP_201_CREATED)
def better_practice_with_response_code():
    return tasksController.better_practice_with_response_code()

# response should be based on model
@task_routes.get("/get-one-specicific-task/{task_id}",response_model=TaskResponseTitleDto, status_code=status.HTTP_200_OK)
def get_one_specicific_task(task_id:int,db=Depends(get_db)):
    return tasksController.get_one_specicific_task(task_id,db)


# reponse of list based on model
@task_routes.get("/get-task-list-limited-keys",response_model=List[TaskResponseTitleDto], status_code=status.HTTP_200_OK)
def get_task_list_limited_keys(db=Depends(get_db)):
    return tasksController.get_task_list_limited_keys(db)

# db type define
@task_routes.get("/get-task-list-limited-keys",response_model=List[TaskResponseTitleDto], status_code=status.HTTP_200_OK)
def get_task_list_limited_keys(db:Session=Depends(get_db)):
    return tasksController.get_task_list_limited_keys(db)
