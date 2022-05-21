from fastapi import FastAPI

from src.cisco.api.routing import api_router

app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome in the Cisco task. To read documentation go to '/docs'"}


app.include_router(api_router)
