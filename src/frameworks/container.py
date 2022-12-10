from dependency_injector import containers, providers

from domain.use_cases.happy_location import HappyLocationUseCase
from domain.use_cases.mood_frequency import MoodFrequencyUseCase
from domain.use_cases.upload_mood_capture import UploadMoodCaptureUseCase
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.repositories.happy_location import HappyLocationRepository
from interface_adapters.data.repositories.mood_frequency import MoodFrequencyRepository
from interface_adapters.data.repositories.upload_mood_capture import (
    UploadMoodCaptureRepository,
)


class FrameworkContainer(containers.DeclarativeContainer):
    """Framework container"""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.routes.health_check",
            "interface_adapters.routes.v1.upload_mood_capture",
            "interface_adapters.routes.v1.user_mood_sensing",
            "main"
        ],
    )

    database_manager: PostgresqlManager = providers.Factory(PostgresqlManager)

    # Repositories
    upload_mood_capture_repository: UploadMoodCaptureRepository = providers.Factory(
        UploadMoodCaptureRepository, database_service=database_manager
    )

    mod_frequency_repository: MoodFrequencyRepository = providers.Factory(
        MoodFrequencyRepository, database_service=database_manager
    )

    happy_location_repository: HappyLocationRepository = providers.Factory(
        HappyLocationRepository, database_service=database_manager
    )
    
    #use cases
    upload_mood_capture_use_case: UploadMoodCaptureUseCase = providers.Factory(
        UploadMoodCaptureUseCase, repository=upload_mood_capture_repository
    )

    mood_frequency_use_case: MoodFrequencyUseCase = providers.Factory(
        MoodFrequencyUseCase, repository=mod_frequency_repository
    )
    
    happy_location_use_case: HappyLocationUseCase = providers.Factory(
        HappyLocationUseCase, repository=happy_location_repository
    )
