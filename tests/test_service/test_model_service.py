from fastapi_skeleton.services.model_service import predict_heart_disease
from fastapi_skeleton.models.payload import HeartDiseaseInput

def test_predict_heart_disease():
    input_data = HeartDiseaseInput(
        age=50, sex=1, chest_pain_type=2, resting_blood_pressure=130,
        cholestoral=220, fasting_blood_sugar=0, rest_ecg=1, Max_heart_rate=150,
        exercise_induced_angina=0, oldpeak=1.5, slope=2, vessels_colored_by_flourosopy=0,
        thalassemia=2
    )
    
    result = predict_heart_disease(input_data)
    assert result in ["Heart Disease Detected", "No Heart Disease"]
