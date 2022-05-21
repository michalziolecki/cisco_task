from fastapi import FastAPI

from src.cisco.api.models.base import HomeModel
from src.cisco.api.routing import api_router

app = FastAPI()


@app.get("/", response_model=HomeModel, tags=["Home"], description="Root path")
async def home() -> HomeModel:
    return HomeModel()


app.include_router(api_router)
