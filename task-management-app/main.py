from fastapi import FastAPI
from src.config.db import Base,engine


Base.metadata.create_all(engine)

app = FastAPI(title="This is a Task Management App")

