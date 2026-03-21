# backend/queries/rec_queries.py

FRIEND_BASED_RECS = """
MATCH (u:User {id: $user_id})-[:FRIEND_OF]->(friend:User)
      -[liked:LIKED]->(movie:Movie)
WHERE NOT (u)-[:LIKED]->(movie)
  AND NOT (u)-[:WATCHED]->(movie)
RETURN movie.title                    AS title,
       count(friend)                  AS liked_by_friends,
       round(avg(liked.rating), 2)    AS avg_rating
ORDER BY liked_by_friends DESC, avg_rating DESC
"""

CONTENT_BASED_RECS = """
MATCH (u:User {id: $user_id})-[:LIKED]->(lm:Movie)
      -[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(rec:Movie)
WHERE NOT (u)-[:LIKED]->(rec)
  AND NOT (u)-[:WATCHED]->(rec)
  AND lm <> rec
RETURN rec.title                      AS title,
       collect(DISTINCT g.name)       AS matched_genres,
       count(DISTINCT g)              AS genre_overlap
ORDER BY genre_overlap DESC
"""

HYBRID_RECS = """
MATCH (u:User {id: $user_id})-[:FRIEND_OF]->(friend:User)
      -[liked:LIKED]->(movie:Movie)
WHERE NOT (u)-[:LIKED]->(movie)
  AND NOT (u)-[:WATCHED]->(movie)
WITH movie,
     count(DISTINCT friend)   AS friend_score,
     avg(liked.rating)        AS avg_rating
OPTIONAL MATCH (u:User {id: $user_id})-[:LIKED]->(lm:Movie)
               -[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(movie)
WITH movie, friend_score, avg_rating,
     count(DISTINCT g) AS genre_score
RETURN movie.title                                          AS title,
       round((friend_score * 0.6) + (genre_score * 0.4), 2) AS hybrid_score
ORDER BY hybrid_score DESC
"""

SHORTEST_PATH = """
MATCH path = shortestPath(
  (a:User {id: $user_id})-[:FRIEND_OF*]-(b:User {id: $target_id})
)
RETURN [node IN nodes(path) | node.name] AS chain,
       length(path)                       AS hops
"""