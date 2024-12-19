from src.database import DatabaseManager

class TagManager:
    @staticmethod
    def add_tag(book_id, tag):
        """Add a tag to a book."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tags (book_id, tag) VALUES (?, ?);",
                (book_id, tag),
            )
            conn.commit()
        return f"Tag '{tag}' added to book ID {book_id}."

    @staticmethod
    def list_tags(book_id):
        """List all tags for a specific book."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT tag FROM tags WHERE book_id = ?;", (book_id,))
            tags = cursor.fetchall()
        if tags:
            return ", ".join(tag[0] for tag in tags)
        return "No tags found."

    @staticmethod
    def delete_tag(book_id, tag):
        """Delete a specific tag from a book."""
        db = DatabaseManager()
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tags WHERE book_id = ? AND tag = ?;",
                (book_id, tag),
            )
            conn.commit()
        return f"Tag '{tag}' removed from book ID {book_id}."
