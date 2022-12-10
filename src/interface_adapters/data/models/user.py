# pylint: disable=R0801,R0902
from __future__ import annotations

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select

from interface_adapters.data.models.base import Model


class UserModel(Model):
    """Database representation for table user"""

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)

    @classmethod
    async def find_by_name(cls, session: AsyncSession, user_name: str) -> int:
        """Find by its id."""
        query: Select = select(cls).filter(cls.user_name == user_name)
        result: Result = await session.execute(query)
        user = result.scalars().first()
        return user.user_id if user else None
