# Reading List Manager

## Overview

**Reading List Manager** is a command-line application designed to assist users in managing their reading lists efficiently. It supports operations like adding, updating, and tracking books, and generating reports. The application leverages SQLite for data storage, following a modular architecture for maintainability and scalability.

---

## Features

- **Book Management**:
  - Add books with details like title, author, year, and reading status.
  - Update the status of books (e.g., "To Read", "Reading", "Completed").
  - View a list of all books.
  - Delete books from the reading list.

- **Tag Management** (Optional future feature):
  - Add, list, or delete tags for books to organize them better.

- **Reports**:
  - Generate reports of your reading list in CSV or Excel format.

- **Command-Line Interface**:
  - Intuitive and menu-driven interface for seamless interaction.

---

## File Structure

```
READING_LIST_MANAGER
│   .gitignore            # Ignores sensitive files and compiled artifacts.
│   app.py                # Entry point for the application CLI.
│   README.md             # Project overview and instructions.
│   requirements.txt      # List of Python dependencies.
│   sample_reading_list.db # Sample database for testing.
│   sample_settings.py    # Example settings configuration.
│
├───src
│   │   cli.py            # Handles user interaction through the command line.
│   │   database.py       # Database connection and table setup.
│   │   __init__.py       # Initializes the package.
│   │
│   ├───data
│   │       reading_list.db  # SQLite database file.
│   │
│   ├───managers
│   │   │   book_manager.py  # Business logic for book-related operations.
│   │   │   tag_manager.py   # Placeholder for future tag-related logic.
│   │   │   __init__.py      # Initializes the managers package.
│   │
│   ├───models
│   │   │   book.py          # Book class managing ORM operations.
│   │   │   __init__.py      # Initializes the models package.
│   │
│   ├───reports
│   │   │   report_generator.py  # Logic for generating CSV and Excel reports.
│   │   │   __init__.py          # Initializes the reports package.
│   │
│   ├───settings
│   │   │   settings.py      # Database path configuration and directory setup.
│   │   │   __init__.py      # Initializes the settings package.
│   │
│   └───__pycache__          # Compiled Python files (ignored via .gitignore).
│
└───tests
    │   note.md             # Notes on the testing framework.
    │   test_book_manager.py # Unit tests for book manager operations.
    │   test_database.py    # Unit tests for database connections and tables.
    │   __init__.py         # Initializes the tests package.
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GeorgeSava30/reading_list_manager
   cd reading_list_manager
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```powershell
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Using the Sample Database and Sample Settings**:
   - The repository includes a `sample_reading_list.db` file with some preloaded data for testing and experimentation.
   - To use it:
     - Rename `sample_settings.py` to `settings.py` and place it in the `src/settings/` directory.
     - Update the `DATABASE_PATH` in `settings.py` to point to the sample database:
       ```python
       DATABASE_PATH = "sample_reading_list.db"
       ```
   - Now, you can start the application with this sample data.

6. **Initialize an Empty Database**:
   - If you'd prefer to start fresh, you can initialize an empty database using the CLI:
     ```bash
     python src/app.py
     ```
   - Select the "Initialize Database" option from the menu. This will create an empty `reading_list.db` file at the path specified in your `settings.py`.

7. **Run the Application**:
   ```bash
   python src/app.py
   ```

---

## Usage

### Commands (via CLI Menu)
1. **Initialize Database**: Set up the required database tables (for a new database).
2. **Add a Book**: Add a book by entering its title, author, publication year, and reading status.
3. **List All Books**: View the complete reading list with details.
4. **Update Book Status**: Modify the reading status of any book by entering its ID and new status.
5. **Delete a Book**: Remove books from your list by entering the ID of the book to delete.
6. **Add a Tag to a Book**: Assign a tag to a book by entering the book's ID and the desired tag.
7. **List Tags for a Book**: Display all tags associated with a specific book by providing its ID.
8. **Delete a Tag from a Book**: Remove a tag from a specific book by entering the book's ID and the tag to delete.
9. **Generate Report**: Export your reading list in either CSV or Excel format by specifying the format and output filename.
0. **Exit**: Close the application.

---

## Tests

The application includes unit tests located in the `tests/` directory, ensuring core functionality like database integrity and book operations. To run tests:

```bash
python -m unittest discover -s tests
```

