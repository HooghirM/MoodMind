
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL = "sqlite:///./test.db" #PLACE HOLDER LINK
    ENVIRONMENT = "Areyana loves my cock"   # Place holder
    SECRET_KEY = "supersecretkey"        # Place holder


settings = Settings()       