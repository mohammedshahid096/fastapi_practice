from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.controllers import userController 
from src.dtos.userDto import CreateUserDTO,CreateUserResponseDTO
user_routes = APIRouter(prefix="/user")


@user_routes.post("/register",response_model=CreateUserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(body:CreateUserDTO,db:Session = Depends(get_db)):
    return userController.register(body,db)
