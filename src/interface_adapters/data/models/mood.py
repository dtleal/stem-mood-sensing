# pylint: disable=R0801,R0902
from __future__ import annotations

import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, text
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from domain.ports.mood_frequency import MoodFrequencyOutputPort
from domain.ports.happy_location import HappyLocationOutputPort
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

    @classmethod
    async def get_mood_frequency(
        cls,
        session: AsyncSession,
        user_id: int
    ) -> MoodFrequencyOutputPort:
        """Get most selled piza."""
        try:
            query = text(
                f'SELECT u.user_name, count(mo.mood) as mood_frequency, mo.mood \
                FROM mood mo join "user" u on mo.user_id = u.user_id where u.user_id = {user_id} \
                GROUP by u.user_name, mo.mood ORDER BY mood_frequency DESC'
            )
            resultset: Result = await session.execute(query)
            result = resultset.fetchall()
            print('resultado: ', result)
            return MoodFrequencyOutputPort(
                result=result
            )
        except Exception as e:
            print("Error: ", e)

    @classmethod
    async def get_happy_location(
        cls,
        session: AsyncSession,
        user_id: int
    ) -> HappyLocationOutputPort:
        """Get most selled piza."""
        try:
            query = text(
                f"SELECT u.user_name, count(mo.mood) as happy_frequency, mo.location \
                from mood mo join public.user u on mo.user_id = u.user_id where u.user_id = {user_id} \
                and mo.mood = 'happy' GROUP by u.user_name, mo.location"
            )
            resultset: Result = await session.execute(query)
            result = resultset.fetchall()
            return HappyLocationOutputPort(
                user_name=result[0][0],
                happy_frequency=result[0][1],
                location=result[0][2],
            )

        except Exception as e:
            print("Error: ", e)
