from fastapi import HTTPException
from src.dtos.taskDto import CreateTaskDTO
from sqlalchemy.orm import Session
from src.models.taskModel import TaskModel

def create_task(body:CreateTaskDTO,db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"],
                         description = data["description"],
                         is_completed = data["is_completed"]
                         )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "status" :201,
        "message" :"task created successfully",
        "data":new_task
    }


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {
        "status" :200,
        "message" : "successfully fetch the tasks",
        "data": tasks
    }


def get_one_task(task_id:int,db:Session): 
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404,"task not found")
    return {
        "status" :200,
        "message" :"Task Fetched Successfully",
        "data" : one_task
    }

def update_task(body:TaskModel,task_id:int,db:Session):
    task_exsit = db.query(TaskModel).get(task_id)
    if not task_exsit:
        raise HTTPException(404,"task not found")

    task_exsit.title = body.title
    task_exsit.description = body.description
    task_exsit.is_completed = body.is_completed

    db.add(task_exsit)
    db.commit()
    db.refresh(task_exsit)

    return {
        "status" : 200,
        "message":"Task Updated successfully",
        "data" : task_exsit
    }
