# Movie Recommender

Project scaffold for a Neo4j-backed FastAPI service.

## Stack
- FastAPI for the API surface
- Neo4j as the graph DB
- Pydantic models for requests/responses

## Structure
- Backend: FastAPI app, routers, and query definitions
	- routers/: feature endpoints (`users`, `movies`, `recommendations`)
	- queries/: Cypher snippets grouped by feature
- scripts: Cypher seed data
- .env: Neo4j connection settings (not committed)

## Quick start
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set environment variables in `.env`.
4. Run the app (example): `uvicorn Backend.main:app --reload`.

## Dev tips
- Keep Cypher in `Backend/queries/` for reuse across routers.
- Use `scripts/seed_data.cypher` to load sample data into Neo4j during setup.
- Add new routers under `Backend/routers/` and include them in `Backend/main.py`.
