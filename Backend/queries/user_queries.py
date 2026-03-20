ADD_USER = """
MERGE (u:User {id: $user_id})
RETURN u
"""

ADD_FRIEND = """
MATCH (u:User {id: $user_id}), (f:User {id: $friend_id})
MERGE (u)-[:FRIENDS_WITH]->(f)
MERGE (f)-[:FRIENDS_WITH]->(u)
RETURN u, f
"""
