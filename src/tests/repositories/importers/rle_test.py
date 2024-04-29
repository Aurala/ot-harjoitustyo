import unittest
from config import settings
from repositories.importers.rle import RLE


class TestUniverse(unittest.TestCase):

    def setUp(self):
        self.importer = RLE()

    def test_can_import_valid_RLE(self):
        name, rules, pattern, metadata = self.importer.read_from_file(
            settings.resources.directory_patterns + "_valid.rle")
        self.assertEqual(name, "Blinker")
        self.assertEqual(rules, "B3/S23")
        self.assertEqual(pattern, [[1, 1, 1]])
        self.assertEqual(
            metadata, "#N Blinker\n#C Valid RLE file for unit testing\n")
