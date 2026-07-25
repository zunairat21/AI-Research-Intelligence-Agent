import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data") / "ai_updates.db"

def get_connection():

    """
        Create and return connection to the sqlite database
    """
    return sqlite3.connect(DATABASE_PATH)
