import csv
import os
from openpyxl import Workbook
from src.models.book import Book

class ReportGenerator:
    @staticmethod
    def generate_report(format="csv", output_path="report"):
        """Generate a report in the specified format (csv or excel)."""
        books = Book.get_all_books()
        if not books:
            print("No books found to generate a report.")
            return

        if format == "csv":
            file_path = f"{output_path}.csv"
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Title", "Author", "Year", "Status"])
                writer.writerows(books)
            print(f"CSV report generated at {file_path}")

        elif format == "excel":
            file_path = f"{output_path}.xlsx"
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Reading List"
            # Add headers
            sheet.append(["ID", "Title", "Author", "Year", "Status"])
            # Add data rows
            for book in books:
                sheet.append(book)
            workbook.save(file_path)
            print(f"Excel report generated at {file_path}")

        else:
            print("Invalid format specified. Use 'csv' or 'excel'.")
