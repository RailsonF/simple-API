from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Saúde da API"])

@health_router.get("/")
def health():
    return {"Saúde da API:" : "OK"}