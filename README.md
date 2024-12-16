# Reading List Manager

## Overview

Reading List Manager is a command-line application designed to help users manage their reading lists. It provides functionality to add, update, and track books, as well as generate reports. The app uses an SQLite database and is structured using modular components for easy maintenance and scalability.

---

## Features

- **Book Management**:
  - Add books with details like title, author, year, and status.
  - Update the reading status of books (e.g., "To Read", "Reading", "Completed").
  - View a list of all books.

- **User Management**:
  - Add and manage user information (optional future feature).

- **Reports**:
  - Generate reports of your reading list in CSV or Excel format.

- **Command-Line Interface**:
  - Simple terminal-based interaction for quick operations.

---

## Project Structure

```
reading_list_manager
|
|-- settings/
|   |-- settings.py  # Placeholder for sensitive configurations.
|
|-- SRC/
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
     *(If it doesn’t work, use the command in `note.txt`)*
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Settings File**:
   - Create a `settings/settings.py` file with the following template:
     ```python
     DATABASE_PATH = "data/reading_list.db"
     ```

6. **Run the Application**:
   ```bash
   python SRC/app.py
   ```

---

## Usage

### Commands
- **Add a Book**:
  Add a book to your reading list with its details.
  ```bash
  python SRC/app.py add --title "Book Title" --author "Author Name" --year 2024 --status "To Read"
  ```

- **View Books**:
  Display all books in your reading list.
  ```bash
  python SRC/app.py list
  ```

- **Update Book Status**:
  Update the reading status of a book.
  ```bash
  python SRC/app.py update --id 1 --status "Completed"
  ```

- **Generate Report**:
  Create a report of your books in CSV or Excel format.
  ```bash
  python SRC/app.py report --format csv
  ```

---
