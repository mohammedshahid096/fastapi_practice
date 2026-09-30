from fastapi import FastAPI
from src.config.db import Base,engine
from src.routes.router import task_routes



Base.metadata.create_all(engine)

app = FastAPI(title="This is a Task Management App")

app.include_router(task_routes)

