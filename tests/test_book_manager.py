import unittest
from src.managers.book_manager import BookManager

class TestBookManager(unittest.TestCase):

    def setUp(self):
        """Initialize the database for testing."""
        BookManager.init_db()

    def test_add_book(self):
        """Test adding a book to the database."""
        response = BookManager.add_book("Test Title", "Test Author", 2024, "To Read")
        self.assertIn("Book 'Test Title' by Test Author added.", response)

    def test_list_books(self):
        """Test listing books."""
        BookManager.add_book("Sample Book", "Sample Author", 2023, "Reading")
        books = BookManager.list_books()
        self.assertIn("Sample Book by Sample Author", books)

    def test_update_book_status(self):
        """Test updating the status of a book."""
        BookManager.add_book("Another Book", "Another Author", 2022, "To Read")
        response = BookManager.update_status(1, "Completed")
        self.assertIn("status updated to 'Completed'", response)

if __name__ == "__main__":
    unittest.main()
