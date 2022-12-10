from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI

from frameworks.container import FrameworkContainer
from frameworks.database.postgres_manager import PostgresqlManager
from frameworks.fast_api.manager import FastApiManager


def initialize() -> FastAPI:
    try:
        app = FastApiManager(app=FastAPI())
        app.initialize_cors()
        app.initialize_limiter()
        app.initialize_routers()
        __initialize_framework_container()
        return app.get_instance()
    except Exception as error:
        raise Exception(
            "An excepetion has ocurred trying to initialize FastApi: ",
            error,
        ) from error


def __initialize_framework_container() -> None:
    container = FrameworkContainer()
    container.database_manager()
    container.wire(modules=[__name__])


@inject
async def startup(
    connector: PostgresqlManager = Provide[FrameworkContainer.database_manager],
) -> None:
    """App startup hook."""
    await connector.connect()


@inject
async def shutdown(
    connector: PostgresqlManager = Provide[FrameworkContainer.database_manager],
) -> None:
    """App shutdown hook."""
    await connector.close()
