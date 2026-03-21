# backend/database.py

from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI      = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def get_session():
    return driver.session()

def close_driver():
    driver.close()
    print("Driver closed!")