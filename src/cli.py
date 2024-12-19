from src.managers.book_manager import BookManager

class CLI:
    @staticmethod
    def display_menu():
        """Display the main menu and handle user input."""
        while True:
            print("\nReading List Manager")
            print("1. Initialize Database")
            print("2. Add a Book")
            print("3. List All Books")
            print("4. Update Book Status")
            print("5. Delete a Book")
            print("6. Add a Tag to a Book")
            print("7. List Tags for a Book")
            print("8. Delete a Tag from a Book")
            print("0. Exit")

            choice = input("Choose an option (0-8): ")

            if choice == "1":
                print(BookManager.init_db())
            elif choice == "2":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = input("Enter the publication year: ")
                status = input("Enter the reading status (default is 'unread'): ") or "unread"
                print(BookManager.add_book(title, author, year, status))
            elif choice == "3":
                print(BookManager.list_books())
            elif choice == "4":
                book_id = input("Enter the ID of the book to update: ")
                status = input("Enter the new status: ")
                print(BookManager.update_status(book_id, status))
            elif choice == "5":
                book_id = input("Enter the ID of the book to delete: ")
                print(BookManager.delete_book(book_id))
            elif choice == "6":
                book_id = input("Enter the ID of the book to add a tag to: ")
                tag = input("Enter the tag: ")
                print(BookManager.add_tag(book_id, tag))
            elif choice == "7":
                book_id = input("Enter the ID of the book to list tags for: ")
                print(f"Tags: {BookManager.list_tags(book_id)}")
            elif choice == "8":
                book_id = input("Enter the ID of the book to remove a tag from: ")
                tag = input("Enter the tag to remove: ")
                print(BookManager.delete_tag(book_id, tag))
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
