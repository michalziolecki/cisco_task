from fastapi import APIRouter

from src.cisco.api.models.response.health import HealthModel


router = APIRouter()


@router.get("/health", response_model=HealthModel, description="Check that application is running")
async def health() -> HealthModel:
    return HealthModel(status=True)
