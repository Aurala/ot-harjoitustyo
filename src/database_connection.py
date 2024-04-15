import sqlite3

# FIX: Database file needs to be configurable
connection = sqlite3.connect('outomaatti.db')
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
