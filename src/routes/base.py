from fastapi import FastAPI, APIRouter,Depends
from helpers.config import get_settings,Settings
from typing import Annotated
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["Base routes"]
)



@base_router.get("/")
async def read_root(app_settings: Annotated[Settings, Depends(get_settings)]):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "message": f"Welcome to the {app_name} application!",
        "version": app_version
        }