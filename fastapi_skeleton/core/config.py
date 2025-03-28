from pydantic_settings import BaseSettings  # Changed import

class Settings(BaseSettings):
    PROJECT_NAME: str = "Heart Disease Prediction API"
    API_V1_STR: str = "/api/v1"
    
    class Config:
        case_sensitive = True

def get_settings() -> Settings:
    return Settings()