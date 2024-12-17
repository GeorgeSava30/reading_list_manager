import click
from src.database import DatabaseManager
from src.models.book import Book

@click.group()
def cli():
    """A simple CLI app for managing a reading list."""
    pass

@cli.command()
def init_db():
    """Initialize the database."""
    db = DatabaseManager()
    db.create_tables()
    click.echo("Database initialized.")

@cli.command()
@click.option('--title', prompt='Title of the book', help='The title of the book.')
@click.option('--author', prompt='Author of the book', help='The author of the book.')
@click.option('--year', prompt='Publication year', type=int, help='The year the book was published.')
@click.option('--status', default='unread', help='Reading status of the book.')
def add_book(title, author, year, status):
    """Add a new book to the reading list."""
    Book.add_book(title, author, year, status)
    click.echo(f"Book '{title}' by {author} added.")

@cli.command()
def list_books():
    """List all books in the reading list."""
    books = Book.get_all_books()
    if books:
        click.echo("\nReading List:")
        for book in books:
            click.echo(f"[ID {book[0]}] {book[1]} by {book[2]} ({book[3]}) - {book[4]}")
    else:
        click.echo("No books found.")

@cli.command()
@click.option('--book-id', prompt='Book ID', type=int, help='The ID of the book to update.')
@click.option('--status', prompt='New status', help='The new reading status of the book.')
def update_status(book_id, status):
    """Update the reading status of a book."""
    Book.update_status(book_id, status)
    click.echo(f"Book ID {book_id} status updated to '{status}'.")

@cli.command()
@click.option('--book-id', prompt='Book ID', type=int, help='The ID of the book to delete.')
def delete_book(book_id):
    """Delete a book from the reading list."""
    Book.delete_book(book_id)
    click.echo(f"Book ID {book_id} deleted.")

if __name__ == '__main__':
    cli()
