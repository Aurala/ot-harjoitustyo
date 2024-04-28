import unittest
from repositories.library_repository import LibraryRepository


class TestLibraryRepository(unittest.TestCase):

    def setUp(self):
        self.library_repository = LibraryRepository()

    def test_categories_are_returned(self):
        self.assertNotEqual(self.library_repository.get_categories(), [])

    def test_patterns_are_returned(self):
        self.assertNotEqual(self.library_repository.get_pattern(1), None)
