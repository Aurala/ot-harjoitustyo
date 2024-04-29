import unittest
from repositories.library_repository import LibraryRepository


class TestLibraryRepository(unittest.TestCase):

    def setUp(self):
        self.library_repository = LibraryRepository()

    def test_categories_are_returned(self):
        self.assertNotEqual(self.library_repository.get_categories(), [])

    def test_patterns_are_returned_by_id(self):
        self.assertNotEqual(self.library_repository.get_pattern_by_id(1), None)

    def test_patterns_are_returned_by_name(self):
        self.assertNotEqual(
            self.library_repository.get_pattern_by_name("Glider"), None)
