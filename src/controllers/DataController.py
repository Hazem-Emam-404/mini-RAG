from controllers.BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
from controllers.ProjectController import ProjectController
import re
import os


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024
        self.ProjectController = ProjectController()

    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        if file.size > self.settings.FILE_MAX_SIZE_MB * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        return True, ResponseSignal.FILE_TYPE_ALLOWED.value

    def generate_unique_filename(self, original_filename: str, project_id: str) -> str:

        project_path = self.ProjectController.get_project_path(project_id)
        cleaned_filename = self.get_clean_filename(original_filename)
        while True:
            random_key = self.generate_random_string()
            full_path = os.path.join(project_path, f"{random_key}_{cleaned_filename}")
            if not os.path.exists(full_path):
                break

        return full_path

    def get_clean_filename(self, filename: str) -> str:
        cleaned_name = re.sub(r"[^\w\.]", "", filename.strip())
        cleaned_name = re.sub(r"\s+", "_", cleaned_name)
        return cleaned_name
