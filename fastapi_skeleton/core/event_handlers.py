from fastapi import FastAPI

def start_app_handler(app: FastAPI):
    print("🚀 Heart Disease Prediction API is starting...")

def stop_app_handler(app: FastAPI):
    print("🛑 Heart Disease Prediction API is shutting down...")
