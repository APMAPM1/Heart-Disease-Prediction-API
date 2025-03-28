from fastapi import APIRouter, HTTPException
from fastapi_skeleton.models.payload import HeartDiseaseInput
from fastapi_skeleton.services.model_service import predict_heart_disease

router = APIRouter()

@router.post("/predict")
def predict(data: HeartDiseaseInput):
    try:
        result = predict_heart_disease(data)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
