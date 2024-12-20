import unittest
from src.database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        """Set up a test database."""
        self.db = DatabaseManager()
        self.db.connect()
        self.db.create_tables()

    def tearDown(self):
        """Clean up by closing the database connection."""
        self.db.close()

    def test_database_connection(self):
        """Test if the database connection is successfully established."""
        conn = self.db.connect()
        self.assertIsNotNone(conn)

    def test_create_tables(self):
        """Ensure tables are created properly."""
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        # Ensure only necessary tables are checked
        self.assertIn(('books',), tables)

if __name__ == "__main__":
    unittest.main()
