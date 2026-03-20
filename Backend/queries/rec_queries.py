RECOMMEND = """
MATCH (u:User {id: $user_id})-[:FRIENDS_WITH]->(:User)-[:LIKES]->(m:Movie)
WHERE NOT EXISTS { (u)-[:LIKES]->(m) }
RETURN m.id AS movie_id
LIMIT $limit
"""
