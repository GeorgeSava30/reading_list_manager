# settings.py
import os

# Define the database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, '..', 'data', 'reading_list.db')

# Ensure the data directory exists
data_dir = os.path.join(BASE_DIR, '..', 'data')
os.makedirs(data_dir, exist_ok=True)
