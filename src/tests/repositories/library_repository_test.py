import unittest
from config import settings
from repositories.library_repository import LibraryRepository


class TestLibraryRepository(unittest.TestCase):

    def setUp(self):
        self.library_repository = LibraryRepository()

    def test_default_categories_are_returned(self):
        self.assertEqual(len(self.library_repository.get_categories()), 11)

    def test_default_patterns_are_returned(self):
        self.assertEqual(len(self.library_repository.get_patterns()), 49)

    def test_default_patterns_are_returned_by_id(self):
        self.assertEqual(self.library_repository.get_pattern_by_id(7).name, "Medusa")

    def test_default_patterns_are_returned_by_name(self):
        self.assertNotEqual(
            self.library_repository.get_pattern_by_name("Glider"), None)

    def test_import_valid_pattern(self):
        self.assertEqual(len(self.library_repository.get_patterns_by_category(1)), 0)
        self.library_repository.import_pattern(settings.resources.directory_patterns + "_valid.rle")
        self.assertEqual(len(self.library_repository.get_patterns_by_category(1)), 1)
