from heart_disease_api.services.models import load_model

def start_app_handler(app) -> callable:
    def startup() -> None:
        load_model()
    return startup

def stop_app_handler(app) -> callable:
    def shutdown() -> None:
        pass
    return shutdown