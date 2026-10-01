from fastapi import FastAPI
from src.config.db import Base,engine
from src.routes.taskRouter import task_routes
from src.routes.userRouter import user_routes



Base.metadata.create_all(engine)

app = FastAPI(title="This is a Task Management App")

# routes
app.include_router(task_routes)
app.include_router(user_routes)


