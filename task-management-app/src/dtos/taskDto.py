
from pydantic import BaseModel


class CreateTaskDTO(BaseModel):
    title:str
    description:str
    is_completed:bool = False