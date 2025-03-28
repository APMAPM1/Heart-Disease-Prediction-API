from pydantic import BaseModel

class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_blood_pressure: int
    cholestoral: int
    fasting_blood_sugar: int
    rest_ecg: int
    Max_heart_rate: int
    exercise_induced_angina: int
    oldpeak: float
    slope: int
    vessels_colored_by_flourosopy: int
    thalassemia: int
