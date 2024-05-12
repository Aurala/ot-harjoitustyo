import os
import json
import sqlite3
from datetime import datetime
from pygame import image
from config import settings
from entities.pattern import Pattern
from entities.category import Category
from database_connection import get_database_connection
from repositories.decoders.rle import RLE


class LibraryRepository:
    """Class manages access to the database and files:

    - Reading patterns from the SQLite database
    - Importing patterns from files into the SQLite database
    - Reading categories from the SQLite database
    - Writing snapshots of the simulation to PNG files
    """

    def __init__(self):
        """Class constructor for creating a new LibraryRepository.

        Terminates the application if the database has not been initialized.
        """
        self._connection = get_database_connection()

        cursor = self._connection.cursor()

        try:
            cursor.execute("SELECT 1 FROM Categories").fetchall()
        except sqlite3.OperationalError as error:
            print("Muista alustaa tietokanta ennen Outomaatti-sovelluksen " +
                  "ajamista: 'poetry invoke run build'")
            raise SystemExit from error

    def get_categories(self):
        """Returns all pattern categories.

        Returns:
            list: All categories as Category objects.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT category_id, name, description FROM Categories")
        rows = cursor.fetchall()

        categories = []
        for row in rows:
            categories.append(Category(row[0], row[1], row[2]))

        return categories

    def get_patterns(self):
        """Returns all patterns.

        Returns:
            list: All patterns as Pattern objects.
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
        """Returns patterns in a specified category.

        Args:
            category_id (int): Category identifier.

        Returns:
            list: Patterns as Pattern objects.
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
        """Returns a pattern based on its identifier.

        Args:
            pattern_id (int): Pattern identifier.

        Returns:
            Pattern: Specified pattern as a Pattern object. (None if not found.)
        """
        sql_command = "SELECT * FROM Patterns WHERE pattern_id=?"

        cursor = self._connection.cursor()
        cursor.execute(sql_command, [pattern_id])
        row = cursor.fetchone()

        if row is None:
            return None

        return Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5])

    def get_pattern_by_name(self, pattern_name):
        """Returns a pattern based on its name.

        Args:
            pattern_name (str): Pattern name.

        Returns:
            Pattern: Specified pattern as a Pattern object. (None if not found.)
        """
        sql_command = "SELECT * FROM Patterns WHERE name=?"

        cursor = self._connection.cursor()
        cursor.execute(sql_command, [pattern_name])
        row = cursor.fetchone()

        if row is None:
            return None

        return Pattern(row[0], row[1], row[2], row[3], json.loads(row[4]), row[5])

    def import_pattern(self, filename, category_id=1):
        """Imports a pattern into the database.

        Currently manages Run-Length Encoded (RLE) files.
        If the extension is not ".rle", does nothing.

        Args:
            filename (str): File containing the pattern.

        Returns:
            bool: Whether the operation was successful or not.
        """
        sql_command = """
                      INSERT INTO Patterns (
                      category_id,
                      name,
                      rules,
                      pattern,
                      metadata
                      ) VALUES (?, ?, ?, ?, ?)
                      """

        if filename.lower().endswith(".rle"):

            decoder = RLE()

            with open(filename, "r", encoding="UTF-8") as rle_file:
                rle_data = rle_file.readlines()

            encoded = decoder.decode(rle_data)
            if encoded is not None:
                cursor = self._connection.cursor()
                cursor.execute(sql_command, [
                    category_id,
                    encoded[0],
                    encoded[1],
                    json.dumps(encoded[2]),
                    encoded[3]
                ])
                self._connection.commit()

            return True

        return False

    def save_snapshot(self, surface):
        """Saves a snapshot of the simulation to a PNG file.

        The current timestamp will be used as the filename.
        The output directory is specified in the settings.
        If the director does not exist, it will be created.

        Args:
            surface (pygame.Surface): Surface containing the image
        """
        directory = settings.resources.directory_snapshots
        if not os.path.exists(directory):
            os.makedirs(directory)
        timestamp = str(datetime.now())
        filename = directory + timestamp + ".png"
        image.save(surface, filename)
