import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_PATH / DB_NAME

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL

# DANGER!: delete without where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# Restarting IDs
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Register values in table columns
# Be careful! (SQL Injection)
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Charles", 69.0)'
)
connection.commit()

# cursor.executemany(
#     f''
# )

cursor.close()
connection.close()