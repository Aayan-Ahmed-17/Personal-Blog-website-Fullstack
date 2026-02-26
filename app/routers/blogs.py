from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World", "status": "success"}

@router.get("/health")
async def health():
    return {"status": "Api is running", "status_code": 200}