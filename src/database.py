import sqlite3
import os
from src.settings.settings import DATABASE_PATH

class DatabaseManager:
    def __init__(self):
        self.connection = None

    def connect(self):
        """Establish connection to the SQLite database."""
        if not self.connection:
            self.connection = sqlite3.connect(DATABASE_PATH)
        return self.connection

    def create_tables(self):
        """Create the required tables if they do not exist."""
        with self.connect() as conn:
            cursor = conn.cursor()
            # Create books table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    status TEXT NOT NULL
                );
            """)
            # Create tags table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER NOT NULL,
                    tag TEXT NOT NULL,
                    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
                );
            """)
            conn.commit()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
