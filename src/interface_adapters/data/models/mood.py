# pylint: disable=R0801,R0902
from __future__ import annotations

import enum

from sqlalchemy import Column, Enum, ForeignKey, String, Integer

from interface_adapters.data.models.base import Model


class MoodEnum(enum.Enum):
    """Mood type enum"""

    HAPPY = "happy"
    SAD = "sad"
    NEUTRAL = "neutral"


class MoodModel(Model):
    """Database representation for table mood"""

    mood_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("user.user_id", ondelete="CASCADE"),
        index=True,
    )
    mood = Column(Enum(MoodEnum))
    location = Column(String)
