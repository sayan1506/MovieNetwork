# backend/models.py

from pydantic import BaseModel
from typing import Optional

# ── Request models ───────────────────────────────────────────

class UserCreate(BaseModel):
    id: str
    name: str
    email: str
    password: str

class FriendRequest(BaseModel):
    user_id: str
    friend_id: str

class LikeMovieRequest(BaseModel):
    user_id: str
    movie_id: str
    rating: float

class MovieCreate(BaseModel):
    id: str
    title: str
    summary: str
    poster_url: Optional[str] = None
    genres: list[str]

# ── Response models ──────────────────────────────────────────

class MovieRecommendation(BaseModel):
    title: str
    score: float

class PathResponse(BaseModel):
    chain: list[str]
    hops: int