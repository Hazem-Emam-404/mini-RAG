from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from typing import Annotated
from controllers.DataController import DataController
from controllers.ProjectController import ProjectController
from models import ResponseSignal
import os
import aiofiles
import logging

data_router = APIRouter(prefix="/api/v1/data", tags=["Data routes"])
logger = logging.getLogger("uvicorn.error")


@data_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile,
    app_settings: Annotated[Settings, Depends(get_settings)],
):
    data_controller = DataController()

    is_valid, message = data_controller.validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "is_valid": is_valid,
                "message": message,
                "project_id": project_id,
            },
        )

    file_path = data_controller.generate_unique_filename(
        original_filename=file.filename, project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, "wb") as out_file:

            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await out_file.write(chunk)
    except Exception as e:
        logger.error(f"Error occurred while saving the file: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "is_valid": is_valid,
                "Signal": ResponseSignal.FILE_UPLOAD_FAILED.value,
                "project_id": project_id,
            },
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "is_valid": is_valid,
            "message": ResponseSignal.FILE_UPLOADED_SUCCESS.value,
            "project_id": project_id,
            "file_path": file_path,
        },
    )
