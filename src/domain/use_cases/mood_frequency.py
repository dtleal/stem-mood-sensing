from domain.interfaces.use_case import UseCase
from domain.ports.mood_frequency import MoodFrequencyOutputPort
from interface_adapters.data.repositories.mood_frequency import MoodFrequencyRepository


class MoodFrequencyUseCase(UseCase):
    """Get mood frequency use case by user"""

    def __init__(self, repository: MoodFrequencyRepository) -> None:
        self._repository = repository

    async def __call__(self, user_name: str) -> MoodFrequencyOutputPort:
        return await self._repository.get_mood_frequency(user_name=user_name)
