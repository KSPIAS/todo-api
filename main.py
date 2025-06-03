# from fastapi import FastAPI
# from routes import router

# app = FastAPI()

# app.include_router(router)

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
# import models, schemas, database #For Test

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
