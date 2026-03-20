from contextlib import contextmanager
from neo4j import GraphDatabase


def create_driver(uri: str, user: str, password: str):
    """Create a Neo4j driver instance."""
    return GraphDatabase.driver(uri, auth=(user, password))


@contextmanager
def get_session(driver):
    """Yield a session and ensure it closes."""
    session = driver.session()
    try:
        yield session
    finally:
        session.close()
