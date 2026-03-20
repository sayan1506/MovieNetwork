from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/add-user")
def add_user():
    return {"detail": "stub"}


@router.post("/add-friend")
def add_friend():
    return {"detail": "stub"}
