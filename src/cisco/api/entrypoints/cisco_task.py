from fastapi import APIRouter, Body

from src.cisco.api.models.body.cisco import SourceModel
from src.cisco.api.models.response.cisco import InfoModel, PingModel
from src.cisco.scraper.utils import get_request_forward_body


router = APIRouter()


@router.get("/info", response_model=InfoModel, description="Hardcoded status")
async def info() -> InfoModel:
    return InfoModel()


@router.post("/ping", response_model=PingModel, description="Forward payload from indicated url")
async def ping(source: SourceModel = Body(...)) -> PingModel:
    result = get_request_forward_body(url=source.url)
    return PingModel(payload=result)
