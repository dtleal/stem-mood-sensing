from sqlalchemy.ext.asyncio import AsyncSession

from domain.ports.upload_mood_capture import (
    UploadMoodCaptureInputPort,
    UploadMoodCaptureOutputPort,
)
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.mood import MoodModel
from interface_adapters.data.models.user import UserModel


class UploadMoodCaptureRepository:
    """Repository to handle with mood capture uploads."""

    def __init__(self, database_service: PostgresqlManager) -> None:
        self._db = database_service

    async def upload_mood_capture(
        self, input_port: UploadMoodCaptureInputPort
    ) -> UploadMoodCaptureOutputPort:
        """Upload mood capture."""
        await self._db.connect()
        async with self._db.session() as session:
            try:
                user_id = await UserModel.find_by_name(
                    session=session, user_name=input_port.user_name
                )

                if not user_id:
                    await self._insert_user(
                        session=session, user_name=input_port.user_name
                    )
                    user_id = await UserModel.find_by_name(
                        session=session, user_name=input_port.user_name
                    )

                await self._insert_mood(
                    session=session, user_id=user_id, input_port=input_port
                )
            except Exception as error:
                raise Exception(f"An error has ocurred: {error}")
        return UploadMoodCaptureOutputPort(
            user_id=user_id,
            user_name=input_port.user_name,
            mood=input_port.mood,
            location=input_port.location,
        )

    @classmethod
    async def _insert_user(self, session: AsyncSession, user_name: str) -> None:
        user = UserModel(user_name=user_name)
        session.add(user)
        await session.commit()

    @classmethod
    async def _insert_mood(
        self,
        session: AsyncSession,
        user_id: int,
        input_port: UploadMoodCaptureInputPort,
    ) -> None:
        mood = MoodModel(
            user_id=user_id, mood=input_port.mood, location=input_port.location
        )
        session.add(mood)
        await session.commit()
