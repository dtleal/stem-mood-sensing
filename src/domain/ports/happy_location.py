# pylint: disable=R0801,R0902
from pydantic.dataclasses import dataclass

from domain.interfaces.output_port import OutputPort


@dataclass
class HappyLocationOutputPort(OutputPort):
    """Object to describe the result of mood upload."""

    user_name: str
    happy_frequency: str
    location: str
