from fastapi import FastAPI

from routers import movies, recommendations, users


app = FastAPI(title="Movie Recommender")

# Attach feature routers
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(recommendations.router)


@app.get("/health")
def health_check():
	return {"status": "ok"}
