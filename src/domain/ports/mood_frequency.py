# pylint: disable=R0801,R0902
from pydantic.dataclasses import dataclass

from domain.interfaces.output_port import OutputPort


@dataclass
class MoodFrequencyOutputPort(OutputPort):
    """Object to describe the result of mood upload."""

    result: list
