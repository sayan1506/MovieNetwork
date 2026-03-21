# backend/queries/user_queries.py

CREATE_USER = """
MERGE (u:User {id: $id})
ON CREATE SET
    u.name      = $name,
    u.email     = $email,
    u.password  = $password,
    u.joined_at = $joined_at
RETURN u.id AS id, u.name AS name, u.email AS email
"""

ADD_FRIEND = """
MATCH (a:User {id: $user_id}), (b:User {id: $friend_id})
MERGE (a)-[:FRIEND_OF {since: $since}]->(b)
MERGE (b)-[:FRIEND_OF {since: $since}]->(a)
RETURN a.name AS user, b.name AS friend
"""

GET_USER = """
MATCH (u:User {id: $id})
RETURN u.id AS id, u.name AS name, u.email AS email
"""