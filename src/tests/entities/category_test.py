import unittest
from entities.category import Category


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.category = Category(1, "Testing - name", "Testing - description")

    def test_property_category_id(self):
        self.assertEqual(self.category.category_id, 1)

    def test_property_name(self):
        self.assertEqual(self.category.name, "Testing - name")

    def test_property_description(self):
        self.assertEqual(self.category.description, "Testing - description")
