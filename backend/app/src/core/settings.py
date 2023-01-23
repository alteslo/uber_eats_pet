from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "UBER EATS PET PROECT"
    VERSION: str = "0.0.1"

    DEBUG: bool

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    DATABASE_URL: str

    LOG_LEVEL: str = "debug"
    LOG_PATH: str = "log"

    LOGGER_ROTATION: str = "5 KB"


settings = Settings()
