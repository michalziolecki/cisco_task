from fastapi import APIRouter


router = APIRouter()


@router.get("/info")
async def info():
    return {"info": "OK"}


@router.get("/ping")
async def ping():
    return {"ping": "OK"}
