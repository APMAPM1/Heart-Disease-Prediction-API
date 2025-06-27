from fastapi.testclient import TestClient
from fastapi_skeleton.main import app

client = TestClient(app)

def test_prediction():
    payload = {
        "age": 50, "sex": 1, "chest_pain_type": 2, "resting_blood_pressure": 130,
        "cholestoral": 220, "fasting_blood_sugar": 0, "rest_ecg": 1, "Max_heart_rate": 150,
        "exercise_induced_angina": 0, "oldpeak": 1.5, "slope": 2, "vessels_colored_by_flourosopy": 0,
        "thalassemia": 2
    }
    
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
