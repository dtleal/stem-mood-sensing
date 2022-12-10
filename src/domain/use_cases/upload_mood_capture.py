from domain.interfaces.use_case import UseCase
from domain.ports.upload_mood_capture import (
    UploadMoodCaptureInputPort,
    UploadMoodCaptureOutputPort,
)
from interface_adapters.data.repositories.upload_mood_capture import (
    UploadMoodCaptureRepository,
)


class UploadMoodCaptureUseCase(UseCase):
    """Upload mood capture use case"""

    def __init__(self, repository: UploadMoodCaptureRepository) -> None:
        self._repository = repository

    async def __call__(
        self, input_use_case: UploadMoodCaptureInputPort
    ) -> UploadMoodCaptureOutputPort:
        return await self._repository.upload_mood_capture(input_port=input_use_case)
