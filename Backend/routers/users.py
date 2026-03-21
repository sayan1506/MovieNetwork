# backend/routers/users.py

from fastapi import APIRouter, HTTPException
from database import get_session
from models import UserCreate, FriendRequest
from queries.user_queries import CREATE_USER, ADD_FRIEND, GET_USER
from queries.rec_queries import SHORTEST_PATH
from datetime import datetime

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def add_user(user: UserCreate):
    with get_session() as session:
        result = session.run(
            CREATE_USER,
            id        = user.id,
            name      = user.name,
            email     = user.email,
            password  = user.password,   # hash this in production
            joined_at = datetime.now().isoformat()
        )
        record = result.single()
        if not record:
            raise HTTPException(status_code=400, detail="User creation failed")
        return {"message": "User created", "user": dict(record)}


@router.post("/friend")
def add_friend(req: FriendRequest):
    with get_session() as session:
        # Check both users exist first
        u1 = session.run(GET_USER, id=req.user_id).single()
        u2 = session.run(GET_USER, id=req.friend_id).single()

        if not u1:
            raise HTTPException(status_code=404,
                                detail=f"User {req.user_id} not found")
        if not u2:
            raise HTTPException(status_code=404,
                                detail=f"User {req.friend_id} not found")

        result = session.run(
            ADD_FRIEND,
            user_id   = req.user_id,
            friend_id = req.friend_id,
            since     = datetime.now().isoformat()
        )
        record = result.single()
        return {
            "message": f"{record['user']} and {record['friend']} are now friends"
        }


@router.get("/path")
def get_path(user_id: str, target_id: str):
    with get_session() as session:
        result = session.run(
            SHORTEST_PATH,
            user_id   = user_id,
            target_id = target_id
        )
        record = result.single()
        if not record:
            raise HTTPException(status_code=404,
                                detail="No path found between these users")
        return {
            "chain": record["chain"],
            "hops":  record["hops"]
        }