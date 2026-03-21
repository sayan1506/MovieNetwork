# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import close_driver
from routers import users, movies, recommendations

app = FastAPI(
    title="Movie Recommender API",
    description="Graph-powered movie recommendations using Neo4j",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(recommendations.router)

@app.on_event("shutdown")
def shutdown():
    close_driver()

@app.get("/")
def root():
    return {"status": "Movie Recommender API is running"}