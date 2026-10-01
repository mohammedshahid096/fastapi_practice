from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    name:str
    username:str
    password:str
    email:str


class CreateUserResponseDTO(BaseModel):
    id:int
    name:str
    username:str
    email:str


class LoginDTO(BaseModel):
    username:str
    password:str


class LoginResponseDTO(BaseModel):
    data:CreateUserResponseDTO
    auth_token:str
