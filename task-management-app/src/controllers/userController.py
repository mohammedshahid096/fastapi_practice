from fastapi import HTTPException
from src.dtos.userDto import CreateUserDTO 
from sqlalchemy.orm import Session
from src.models.userModel import UserModel
from src.utils.passwordUtil import get_password_hash



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



    


     

    
    return {"message":"sucessfully registered a new user"}