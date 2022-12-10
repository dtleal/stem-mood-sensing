# pylint: disable=R0801,R0902
from pydantic.dataclasses import dataclass

from domain.interfaces.input_port import InputPort


@dataclass
class UploadMoodCaptureInputPort(InputPort):
    """Object to describe the result of mood upload."""

    user_id: int
    user_name: str
    mood: str
    location: str


@dataclass
class UploadMoodCaptureOutputPort(InputPort):
    """Object to describe the result of mood upload."""

    user_id: int
    user_name: str
    mood: str
    location: str
