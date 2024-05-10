import json
import sqlite3
from entities.pattern import Pattern
from entities.category import Category
from database_connection import get_database_connection


class LibraryRepository:
    """
    Class manages all access to the persistent storage for the application:
    - Reading and writing patterns and categories SQLite database
    - Reading RLE files containing patterns
    - Writing snapshots of the simulation to PNG files
    """

    def __init__(self):
        """
        Class constructor creates a new LibraryRepository with database
        access configured in the settings file.
        """
        self._connection = get_database_connection()

        cursor = self._connection.cursor()

        try:
            cursor.execute("SELECT 1 FROM Categories").fetchall()
        except sqlite3.OperationalError as error:
            print("Muista alustaa tietokanta ennen Outomaatti-sovelluksen ajamista:",
                  "'poetry invoke run build'")
            raise SystemExit from error

    # FIX: remove duplicate code, the methods below can use same functionalities

    def get_categories(self):
        """
        Returns all pattern categories.

        Returns:
            list: all categories as Category objects
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT category_id, name, description FROM Categories")
        rows = cursor.fetchall()

        categories = []
        for row in rows:
            categories.append(Category(row[0], row[1], row[2]))

        return categories

    def get_patterns(self):
        """
        Returns all patterns.

        Returns:
            list: all patterns as Pattern objects
        """

        sql_command = "SELECT * FROM Patterns"

        cursor = self._connection.cursor()
        cursor.execute(sql_command)
        rows = cursor.fetchall()

        patterns = []
        for row in rows:
            patterns.append(
                Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5]))

        return patterns

    def get_patterns_by_category(self, category_id):
        """
        Returns all patterns in the specified category.

        Returns:
            list: all patterns in the category as Pattern objects
        """

        sql_command = "SELECT * FROM Patterns WHERE category_id=?"

        cursor = self._connection.cursor()
        cursor.execute(sql_command, [category_id])
        rows = cursor.fetchall()

        patterns = []
        for row in rows:
            patterns.append(
                Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5]))

        return patterns

    def get_pattern_by_id(self, pattern_id):
        """
        Returns one category based on its identifier.

        Returns:
            Category: specified category
        """

        sql_command = "SELECT * FROM Patterns WHERE pattern_id=?"

        cursor = self._connection.cursor()
        cursor.execute(sql_command, [pattern_id])
        row = cursor.fetchone()

        if row is None:
            return None

        return Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5])

    def get_pattern_by_name(self, name):
        """
        Returns one category based on its name.

        Returns:
            Category: specified category
        """

        sql_command = "SELECT * FROM Patterns WHERE name=?"

        cursor = self._connection.cursor()
        cursor.execute(sql_command, [name])
        row = cursor.fetchone()

        if row is None:
            return None

        return Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5])
