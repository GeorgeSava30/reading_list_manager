from src.models.book import Book
from src.database import DatabaseManager
from src.managers.tag_manager import TagManager

class BookManager:
    def init_db():
        """Initialize the database."""
        db = DatabaseManager()
        db.create_tables()
        return "Database initialized."

    def add_book(title, author, year, status="unread"):
        """Add a new book to the reading list."""
        Book.add_book(title, author, int(year), status)
        return f"Book '{title}' by {author} added."

    def list_books():
        """List all books in the reading list."""
        books = Book.get_all_books()
        if books:
            formatted_books = []
            for book in books:
                tags = TagManager.list_tags(book[0])
                formatted_books.append(
                    f"[ID {book[0]}] {book[1]} by {book[2]} ({book[3]}) - {book[4]} | Tags: {tags}"
                )
            return "\n".join(formatted_books)
        return "No books found."

    def update_status(book_id, status):
        """Update the reading status of a book."""
        Book.update_status(int(book_id), status)
        return f"Book ID {book_id} status updated to '{status}'."

    def delete_book(book_id):
        """Delete a book from the reading list."""
        Book.delete_book(int(book_id))
        return f"Book ID {book_id} deleted."

    def add_tag(book_id, tag):
        """Add a tag to a book."""
        return TagManager.add_tag(book_id, tag)

    def list_tags(book_id):
        """List all tags for a specific book."""
        return TagManager.list_tags(book_id)

    def delete_tag(book_id, tag):
        """Delete a specific tag from a book."""
        return TagManager.delete_tag(book_id, tag)
