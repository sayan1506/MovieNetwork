from typing import List
from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: str


class FriendLink(BaseModel):
    user_id: str
    friend_id: str


class MovieCreate(BaseModel):
    movie_id: str
    title: str


class LikeMovie(BaseModel):
    user_id: str
    movie_id: str


class RecommendationRequest(BaseModel):
    user_id: str
    limit: int = 5


class RecommendationResponse(BaseModel):
    movies: List[str]
