import os

from backend.app.src.core.settings import settings
from loguru import logger


logger.add(
    sink=os.path.join(settings.LOG_PATH, "log_api_{time}"),
    format="{time} {level} {message}",
    level=settings.LOG_LEVEL,
    rotation=settings.LOGGER_ROTATION
)
