import unittest
from entities.pattern import Pattern


class TestPattern(unittest.TestCase):

    def setUp(self):
        self.pattern = Pattern(
            1, 2, "Testing - name", "Testing - rules", [[1, 1, 1]], "Testing - metadata")

    def test_returns_property_pattern_id(self):
        self.assertEqual(self.pattern.pattern_id, 1)

    def test_returns_property_category_id(self):
        self.assertEqual(self.pattern.category_id, 2)

    def test_returns_property_name(self):
        self.assertEqual(self.pattern.name, "Testing - name")

    def test_returns_property_rules(self):
        self.assertEqual(self.pattern.rules, "Testing - rules")

    def test_return_property_pattern(self):
        self.assertEqual(self.pattern.pattern, [[1, 1, 1]])

    def test_return_property_metadata(self):
        self.assertEqual(self.pattern.metadata, "Testing - metadata")
