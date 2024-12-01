from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Cyber Guardians API"
    database_url: str
    jwt_algorithm: str = "HS256"
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
