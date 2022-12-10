from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class HappyLocationInputDTO(BaseModel):
    """HappyLocation DTO"""

    user_name: str = Field(default=None)


class HappyLocationOutputDTO(BaseModel):
    """HappyLocationOutputCapture DTO"""

    user_name: str = Field(default=None)
    happy_frequency: int = Field(default=None)
    location: str = Field(default=None)
