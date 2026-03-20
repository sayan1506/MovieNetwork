ADD_MOVIE = """
MERGE (m:Movie {id: $movie_id})
SET m.title = $title
RETURN m
"""

LIKE_MOVIE = """
MATCH (u:User {id: $user_id}), (m:Movie {id: $movie_id})
MERGE (u)-[:LIKES]->(m)
RETURN u, m
"""
