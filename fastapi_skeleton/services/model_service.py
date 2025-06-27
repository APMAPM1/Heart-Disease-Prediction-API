import joblib
import pandas as pd
from fastapi_skeleton.models.payload import HeartDiseaseInput

# Load model
model = joblib.load("sample_model/Heart_disease_prediction(knn).joblib")

def predict_heart_disease(data: HeartDiseaseInput) -> str:
    input_data = [[
        data.age, data.sex, data.chest_pain_type, data.resting_blood_pressure,
        data.cholestoral, data.fasting_blood_sugar, data.rest_ecg, data.Max_heart_rate,
        data.exercise_induced_angina, data.oldpeak, data.slope, data.vessels_colored_by_flourosopy,
        data.thalassemia
    ]]

    input_df = pd.DataFrame(input_data, columns=HeartDiseaseInput.model_fields.keys())
    prediction = model.predict(input_df)
    return "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
