# backend/routers/recommendations.py

from fastapi import APIRouter, HTTPException, Query
from database import get_session
from queries.rec_queries import (
    FRIEND_BASED_RECS,
    CONTENT_BASED_RECS,
    HYBRID_RECS
)

router = APIRouter(prefix="/recommend", tags=["Recommendations"])


@router.get("/friends/{user_id}")
def friend_recommendations(user_id: str):
    with get_session() as session:
        result = session.run(FRIEND_BASED_RECS, user_id=user_id)
        records = result.data()
        if not records:
            return {"message": "No friend-based recommendations found",
                    "recommendations": []}
        return {"recommendations": records}


@router.get("/content/{user_id}")
def content_recommendations(user_id: str):
    with get_session() as session:
        result = session.run(CONTENT_BASED_RECS, user_id=user_id)
        records = result.data()
        if not records:
            return {"message": "No content-based recommendations found",
                    "recommendations": []}
        return {"recommendations": records}


@router.get("/hybrid/{user_id}")
def hybrid_recommendations(user_id: str):
    with get_session() as session:
        result = session.run(HYBRID_RECS, user_id=user_id)
        records = result.data()
        if not records:
            return {"message": "No hybrid recommendations found",
                    "recommendations": []}
        return {"recommendations": records}