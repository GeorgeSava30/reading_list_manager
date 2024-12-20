from src.database import DatabaseManager

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
    def get_all_books_with_tags():
        """Retrieve all books with their associated tags."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT b.id, b.title, b.author, b.year, b.status, 
                    GROUP_CONCAT(t.tag, ', ') AS tags
                FROM books b
                LEFT JOIN tags t ON b.id = t.book_id
                GROUP BY b.id;
            """)
            rows = cursor.fetchall()
            books = []
            for row in rows:
                books.append({
                    "id": row[0],
                    "title": row[1],
                    "author": row[2],
                    "year": row[3],
                    "status": row[4],
                    "tags": row[5].split(", ") if row[5] else []
                })
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
