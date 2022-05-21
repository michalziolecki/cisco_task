from fastapi import FastAPI
import uvicorn

from api.api import api_router


app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome in the Cisco task." " To read documentation go to '/docs'"}


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000, log_level="debug")
