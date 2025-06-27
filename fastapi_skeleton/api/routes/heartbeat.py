from fastapi import APIRouter

router = APIRouter()

@router.get("/heartbeat")
def heartbeat():
    return {"status": "API is running"}
