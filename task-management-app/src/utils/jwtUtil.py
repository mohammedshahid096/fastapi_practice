import jwt
from src.config.settings import settings
from datetime import datetime,timedelta

def generate_auth_token(id,username):
    payload = {
        "_id": id,
        "username": username

    }

    ALGORITHM = "HS256"
    EXP_TIME = 30 # 30 min

    exp_time = datetime.now() + timedelta(minutes=EXP_TIME)
    payload["exp"] = exp_time
    
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm = ALGORITHM)
    return token
