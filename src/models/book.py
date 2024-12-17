from SRC.database import DatabaseManager

class Book:
    def __init__(self, title, author, year, status="unread"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @staticmethod
    def add_book(title, author, year, status="unread"):
        """Add a new book to the database."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?);",
                (title, author, year, status),
            )
            conn.commit()

    @staticmethod
    def get_all_books():
        """Retrieve all books from the database."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books;")
            books = cursor.fetchall()
        return books

    @staticmethod
    def update_status(book_id, status):
        """Update the reading status of a book."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE books SET status = ? WHERE id = ?;", (status, book_id)
            )
            conn.commit()

    @staticmethod
    def delete_book(book_id):
        """Delete a book from the database."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?;", (book_id,))
            conn.commit()
