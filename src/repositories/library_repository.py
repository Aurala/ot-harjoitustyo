from entities.pattern import Pattern
from entities.category import Category
from database_connection import get_database_connection


class LibraryRepository:

    def __init__(self):
        self._connection = get_database_connection()

    def get_categories(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT category_id, name, description FROM Categories")
        rows = cursor.fetchall()

        categories = []
        for row in rows:
            categories.append(Category(row[0], row[1], row[2]))

        return categories

    def get_patterns(self, category_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT pattern_id, category_id, name, rules, pattern, metadata FROM Patterns WHERE category_id=?", [category_id])
        rows = cursor.fetchall()

        patterns = []
        for row in rows:
            patterns.append(
                Pattern(row[0], row[1], row[2], row[3], row[4], row[5]))

        return patterns

    def get_pattern(self, pattern_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT pattern_id, category_id, name, rules, pattern, metadata FROM Patterns WHERE pattern_id=?", [pattern_id])
        row = cursor.fetchone()

        if row is None:
            return None
        else:
            return Pattern(row[0], row[1], row[2], row[3], row[4], row[5])

    def save_pattern(self, pattern):
        pass
