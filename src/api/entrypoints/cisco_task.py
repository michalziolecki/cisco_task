from fastapi import APIRouter


router = APIRouter()


@router.get("/info")
async def info():
    return {"info": "OK"}


@router.get("/ping")
async def health():
    return {"ping": "OK"}
