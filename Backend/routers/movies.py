# backend/routers/movies.py

from fastapi import APIRouter, HTTPException
from database import get_session
from models import MovieCreate, LikeMovieRequest
from queries.movie_queries import CREATE_MOVIE, LIKE_MOVIE
from datetime import datetime

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/")
def add_movie(movie: MovieCreate):
    with get_session() as session:
        result = session.run(
            CREATE_MOVIE,
            id         = movie.id,
            title      = movie.title,
            summary    = movie.summary,
            poster_url = movie.poster_url or "",
            genres     = movie.genres
        )
        record = result.single()
        if not record:
            raise HTTPException(status_code=400, detail="Movie creation failed")
        return {"message": "Movie created", "movie": dict(record)}


@router.post("/like")
def like_movie(req: LikeMovieRequest):
    if not (1.0 <= req.rating <= 5.0):
        raise HTTPException(status_code=400,
                            detail="Rating must be between 1.0 and 5.0")
    with get_session() as session:
        result = session.run(
            LIKE_MOVIE,
            user_id  = req.user_id,
            movie_id = req.movie_id,
            rating   = req.rating,
            liked_at = datetime.now().isoformat()
        )
        record = result.single()
        if not record:
            raise HTTPException(status_code=404,
                                detail="User or Movie not found")
        return {
            "message": f"{record['user']} liked {record['movie']}",
            "rating":  record["rating"]
        }