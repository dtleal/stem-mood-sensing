from dependency_injector import containers, providers

from domain.use_cases.upload_mood_capture import UploadMoodCaptureUseCase
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.repositories.upload_mood_capture import (
    UploadMoodCaptureRepository,
)


class FrameworkContainer(containers.DeclarativeContainer):
    """Framework container"""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.routes.health_check",
            "interface_adapters.routes.v1.upload_mood_capture",
            "main"
        ],
    )

    database_manager: PostgresqlManager = providers.Factory(PostgresqlManager)

    # Repositories
    upload_mood_capture_repository: UploadMoodCaptureRepository = providers.Factory(
        UploadMoodCaptureRepository, database_service=database_manager
    )

    upload_mood_capture_use_case: UploadMoodCaptureUseCase = providers.Factory(
        UploadMoodCaptureUseCase, repository=upload_mood_capture_repository
    )
