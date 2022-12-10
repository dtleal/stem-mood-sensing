from domain.ports.happy_location import HappyLocationOutputPort
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.mood import MoodModel
from interface_adapters.data.models.user import UserModel


class HappyLocationRepository:
    """Repository to handle with mood capture uploads."""

    def __init__(self, database_service: PostgresqlManager) -> None:
        self._db = database_service

    async def get_happy_location(self, user_name: str) -> HappyLocationOutputPort:
        """Get happy location by user."""
        await self._db.connect()
        async with self._db.session() as session:
            user_id = await UserModel.find_by_name(session=session, user_name=user_name)
            if result := await MoodModel.get_happy_location(
                session=session, user_id=user_id
            ):
                return result
        return await result
