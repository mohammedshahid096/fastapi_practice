from fastapi import HTTPException
from src.dtos.userDto import CreateUserDTO, LoginDTO 
from sqlalchemy.orm import Session
from src.models.userModel import UserModel
from src.utils.passwordUtil import get_password_hash,verify_password
from src.utils.jwtUtil import generate_auth_token


# for register  a user api
def register(body:CreateUserDTO,db:Session):
    is_user_exist = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user_exist:
        raise HTTPException(400,"username already exist")

    is_user_exist = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user_exist:
        raise HTTPException(400,"email already exist")


    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name =  body.name,
        username = body.username,
        email = body.email,
        hash_password = hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def login(body:LoginDTO,db:Session):
    is_user_exist = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not is_user_exist:
        raise HTTPException(404,"email or password is incorrect")

    is_verified_password = verify_password(body.password,is_user_exist.hash_password)
    if not is_verified_password:
        raise HTTPException(404,"email or password is incorrect")

    


    auth_tokem = generate_auth_token(id=is_user_exist.id,username=is_user_exist.username)

    return {
        "data": is_user_exist,
        "auth_token": auth_tokem
    }

    
        
