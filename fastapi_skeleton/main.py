from fastapi import FastAPI
from fastapi_skeleton.api.routes.router import api_router

app = FastAPI(title="Heart Disease Prediction API")

app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "Welcome to Heart Disease Prediction"}
