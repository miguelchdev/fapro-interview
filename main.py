from fastapi import FastAPI
from router import uf_get
from db.database import engine
from db import models


app = FastAPI()
app.include_router(uf_get.router)

models.Base.metadata.create_all(engine)