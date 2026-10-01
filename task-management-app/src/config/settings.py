from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

    # DB
    DB_CONNECTION_URL:str

    # JWT
    JWT_SECRET_KEY: str = "default-secret-key"


settings = Settings()