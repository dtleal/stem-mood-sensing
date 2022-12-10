from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class MoodFrequencyInputDTO(BaseModel):
    """MoodFrequency DTO"""

    user_name: str = Field(default=None)


class MoodFrequencyOutputDTO(BaseModel):
    """MoodFrequencyOutputCapture DTO"""

    result: list = Field(default=None)
