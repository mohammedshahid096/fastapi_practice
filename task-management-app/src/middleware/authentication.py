from fastapi import Request, HTTPException, status, Depends
from src.utils.jwtUtil import verify_auth_token
from sqlalchemy.orm import Session
from src.models.userModel import UserModel
from src.config.db import get_db

def Authentication(request:Request,db:Session = Depends(get_db)):
    authToken = request.headers.get("Authorization")
    if not (authToken):
        raise HTTPException( status.HTTP_401_UNAUTHORIZED, "auth token is missing")


    token = authToken.split(" ")[-1]

    if not(token):
        raise HTTPException( status.HTTP_401_UNAUTHORIZED, "auth token is missing")

    encodedData = verify_auth_token(token)

    if encodedData is None:
        raise HTTPException( status.HTTP_401_UNAUTHORIZED, "invalid auth token")

    userId = encodedData.get("_id")
    # userName = encodedData.get("username")


    dbUser = db.query(UserModel).filter(UserModel.id == userId).first()

    if not dbUser:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "unuthorized access, user not found")

    return dbUser


def Authorization(allowed_roles:list[str]):
    def check_authorization(user= Depends(Authentication)):
        currentRole = "user"
        # currentRole = user.role
        if currentRole not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to access this resource"
            )

        return user
    return check_authorization