from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Knowledge Assistant"
    API_V1_STR: str = "/api/v1"
    SUPABASE_URL: str
    SUPABASE_KEY: str
    JWT_SECRET: str
    JWT_ALGORITHM:str
    OPENAI_API_KEY: str
    VECTOR_DB_URL: str
    REDIS_URL: str
    OPENROUTER_BASE_URL: str


    class Config:
        env_file = ".env"


settings = Settings()