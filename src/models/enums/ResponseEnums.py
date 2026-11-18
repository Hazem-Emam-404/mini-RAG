from enum import Enum


class ResponseSignal(Enum):
    FILE_UPLOADED_SUCCESS = "File uploaded successfully."
    FILE_UPLOADED_FAILURE = "File upload failed."
    FILE_TYPE_NOT_ALLOWED = "File type not allowed."
    FILE_TYPE_ALLOWED = "File type allowed."
    FILE_SIZE_EXCEEDED = "File size exceeds the maximum allowed size."