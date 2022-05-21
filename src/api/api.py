from fastapi import APIRouter

# from api.entrypoints import home
from api.entrypoints import cisco_task, diagnostics


BASE_PREFIX = "/v1"

api_router = APIRouter()
api_router.include_router(diagnostics.router, prefix="/_", tags=["Diagnostics"])
api_router.include_router(cisco_task.router, prefix=f"{BASE_PREFIX}", tags=["CiscoTask"])
# api_router.add_route(home.router, prefix="", tags=["Home"])
