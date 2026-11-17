from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["Base routes"]
)



@base_router.get("/")
def read_root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": f"Welcome to the {app_name} application!",
        "version": app_version
        }