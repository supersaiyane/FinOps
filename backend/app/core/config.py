from app.core.secrets import secrets_provider

class Settings:
    DB_USER = secrets_provider.get_secret("POSTGRES_USER")
    DB_PASSWORD = secrets_provider.get_secret("POSTGRES_PASSWORD")
    DB_NAME = secrets_provider.get_secret("POSTGRES_DB")
    DB_HOST = "postgres"
    DB_PORT = "5432"

settings = Settings()
