from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class UploadMoodCaptureInputDTO(BaseModel):
    """UploadMoodCapture DTO"""

    user_name: str = Field(default=None)
    mood: str = Field(default=None)
    location: str = Field(default=None)


class UploadMoodCaptureOutputDTO(BaseModel):
    """UploadMoodCapture DTO"""

    user_id: int = Field(default=None)
    user_name: str = Field(default=None)
    mood: str = Field(default=None)
    location: str = Field(default=None)
