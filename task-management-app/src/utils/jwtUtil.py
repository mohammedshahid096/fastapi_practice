import jwt
from jwt.exceptions import InvalidTokenError
from src.config.settings import settings
from datetime import datetime,timedelta

ALGORITHM = "HS256"

def generate_auth_token(id,username):
    payload = {
        "_id": id,
        "username": username

    }

    EXP_TIME = 30 # 30 min

    exp_time = datetime.now() + timedelta(minutes=EXP_TIME)
    payload["exp"] = exp_time
    
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm = ALGORITHM)
    return token


def verify_auth_token(token):
    try:
        data = jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=ALGORITHM)
        return data
    except InvalidTokenError:
        return None
    except jwt.PyJWTError:
        return None
