from domain.interfaces.use_case import UseCase
from domain.ports.happy_location import HappyLocationOutputPort
from interface_adapters.data.repositories.happy_location import HappyLocationRepository


class HappyLocationUseCase(UseCase):
    """Happy location use case by user"""

    def __init__(self, repository: HappyLocationRepository) -> None:
        self._repository = repository

    async def __call__(self, user_name: str) -> HappyLocationOutputPort:
        return await self._repository.get_happy_location(user_name=user_name)
