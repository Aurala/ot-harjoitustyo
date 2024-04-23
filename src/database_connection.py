import sqlite3
from config import settings


# FIX: Database file needs to be configurable
connection = sqlite3.connect(settings.resources.file_database)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
