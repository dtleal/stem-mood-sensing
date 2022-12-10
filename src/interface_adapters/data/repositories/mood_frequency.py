from domain.ports.mood_frequency import MoodFrequencyOutputPort
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.mood import MoodModel
from interface_adapters.data.models.user import UserModel


class MoodFrequencyRepository:
    """Repository to handle with mood capture uploads."""

    def __init__(self, database_service: PostgresqlManager) -> None:
        self._db = database_service

    async def get_mood_frequency(self, user_name: str) -> MoodFrequencyOutputPort:
        """Get mood frequency by user."""
        await self._db.connect()
        async with self._db.session() as session:
            user_id = await UserModel.find_by_name(session=session, user_name=user_name)
            if result := await MoodModel.get_mood_frequency(
                session=session, user_id=user_id
            ):
                return result
        return await result
