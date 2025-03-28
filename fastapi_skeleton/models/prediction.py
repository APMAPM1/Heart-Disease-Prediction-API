from pydantic import BaseModel

class HeartDiseaseResult(BaseModel):
    prediction: str