"""Neo4j connection helper. Credentials are read from .env (never committed)."""
import os
import ssl

import truststore
from dotenv import find_dotenv, load_dotenv
from neo4j import GraphDatabase

load_dotenv(find_dotenv(usecwd=True))


def get_driver():
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")
    if not (uri and user and password):
        raise SystemExit(
            "Missing NEO4J_URI / NEO4J_USERNAME / NEO4J_PASSWORD. "
            "Copy .env.example to .env and fill in your Aura credentials."
        )
    uri = uri.replace("neo4j+s://", "neo4j://").replace("bolt+s://", "bolt://")
    ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    return GraphDatabase.driver(uri, auth=(user, password), ssl_context=ssl_context)


def get_database():
    return os.getenv("NEO4J_DATABASE") or "neo4j"
