import unittest
from entities.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.empty_library = Library([], [], [])

    def test_empty_library_returns_categories_list(self):
        self.assertEqual(self.empty_library.get_categories(), [])

    def test_empty_library_returns_patterns_list(self):
        self.assertEqual(self.empty_library.get_patterns(), [])

    def test_empty_library_returns_rules_list(self):
        self.assertEqual(self.empty_library.get_rules(), [])
