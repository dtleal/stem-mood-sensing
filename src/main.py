import logging
import sys

import application

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s %(filename)s %(funcName)s: %(message)s",
    level=logging.INFO,
)

app = application.initialize()


@app.on_event("startup")
async def startup_event() -> None:
    """FastAPI App startup hook."""
    await application.startup()
    logging.info("FastAPI startup")


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """FastAPI App shutdown hook."""
    await application.shutdown()
    logging.info("FastAPI shutdown")
