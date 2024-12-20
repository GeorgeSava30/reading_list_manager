# Reading List Manager

## Overview

Reading List Manager is a command-line application designed to help users manage their reading lists. It provides functionality to add, update, and track books, as well as generate reports. The app uses an SQLite database and is structured using modular components for easy maintenance and scalability.

---

## Features

- **Book Management**:
  - Add books with details like title, author, year, and status.
  - Update the reading status of books (e.g., "To Read", "Reading", "Completed").
  - View a list of all books.
  - Delete books from the reading list.

- **Reports**:
  - Generate reports of your reading list in CSV or Excel format.

- **Command-Line Interface**:
  - Intuitive menu-driven interaction for quick operations.

---

## Project Structure

```
reading_list_manager
|
|-- settings/
|   |-- settings.py  # Placeholder for sensitive configurations.
|
|-- src/
|   |-- app.py       # Main CLI for interacting with the application.
|   |-- database.py  # Database setup and connection management.
|   |-- __init__.py  # Package initializer.
|
|-- models/
|   |-- book.py      # Book class for database operations.
|   |-- __init__.py  # Package initializer.
|
|-- reports/
|   |-- report_generator.py  # Logic for report generation.
|   |-- __init__.py  # Package initializer.
|
|-- tests/
|   |-- note.txt     # Placeholder for future tests.
|
|-- sample_reading_list.db  # Sample database file for testing.
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/reading_list_manager.git
   cd reading_list_manager
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```powershell
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Settings File**:
   - Create a `settings/settings.py` file with the following content:
     ```python
     DATABASE_PATH = "data/reading_list.db"
     ```

6. **Run the Application**:
   ```bash
   python src/app.py
   ```

---

## Usage

### Commands (via CLI Menu)
- **Initialize Database**:
  Set up the database for the first time.
- **Add a Book**:
  Add a new book to your reading list.
- **List All Books**:
  View the books in your reading list.
- **Update Book Status**:
  Change the reading status of a book.
- **Delete a Book**:
  Remove a book from your list.
- **Generate Report**:
  Export your reading list as CSV or Excel.
- **Exit**:
  Close the application.

---

