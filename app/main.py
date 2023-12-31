from fastapi import FastAPI
import models as models
from config import engine
import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router.router, prefix="/api/v1", tags=["api"])

"""
This is the main module of the FastAPI CRUD PostgreSQL application.
It initializes the FastAPI app, creates the database tables using the models, and includes the router for API endpoints.
"""
