# backend/queries/movie_queries.py

CREATE_MOVIE = """
MERGE (m:Movie {id: $id})
ON CREATE SET
    m.title      = $title,
    m.summary    = $summary,
    m.poster_url = $poster_url
WITH m
UNWIND $genres AS genre_name
    MERGE (g:Genre {name: genre_name})
    MERGE (m)-[:HAS_GENRE]->(g)
RETURN m.id AS id, m.title AS title
"""

LIKE_MOVIE = """
MATCH (u:User {id: $user_id}), (m:Movie {id: $movie_id})
MERGE (u)-[r:LIKED]->(m)
ON CREATE SET r.rating   = $rating,
              r.liked_at = $liked_at
ON MATCH SET  r.rating   = $rating
RETURN u.name AS user, m.title AS movie, r.rating AS rating
"""