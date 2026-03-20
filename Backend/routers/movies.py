from fastapi import APIRouter

router = APIRouter(prefix="/movies", tags=["movies"])


@router.post("/add-movie")
def add_movie():
    return {"detail": "stub"}


@router.post("/like-movie")
def like_movie():
    return {"detail": "stub"}
