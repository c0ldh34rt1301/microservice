from importlib.util import find_spec
from pydantic import AnyHttpUrl, BaseSettings
from typing import List


class Settings(BaseSettings):
    SERVER_NAME: str
    MODEL_LLM: str
    MODEL_URL: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[str] = []
    IVY_URL:  AnyHttpUrl


settings = Settings()