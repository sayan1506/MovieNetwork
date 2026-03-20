from fastapi import APIRouter

router = APIRouter(prefix="/recommend", tags=["recommendations"])


@router.get("")
def recommend():
    return {"movies": []}
