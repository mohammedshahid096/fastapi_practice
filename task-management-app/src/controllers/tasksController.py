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