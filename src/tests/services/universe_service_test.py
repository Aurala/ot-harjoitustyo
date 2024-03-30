import unittest
from services.universe_service import UniverseService

class TestUniverseService(unittest.TestCase):

    def setUp(self):
        self.universe_service = UniverseService()

    def test_create_service_with_default_parameters(self):
        self.assertEqual(self.universe_service.get_textual_presentation(), ".....\n.....\n.....\n.....\n.....\n")
        self.assertEqual(self.universe_service.get_width(), 5)
        self.assertEqual(self.universe_service.get_height(), 5)

    def test_create_service_with_universe_of_4x5(self):
        universe_service = UniverseService(4, 5)
        self.assertEqual(universe_service.get_textual_presentation(), "....\n....\n....\n....\n....\n")
        self.assertEqual(universe_service.get_width(), 4)
        self.assertEqual(universe_service.get_height(), 5)

    def test_add_cell_to_universe(self):
        universe_service = UniverseService(1, 1)
        universe_service.add_cell(0, 0)
        self.assertEqual(universe_service.get_textual_presentation(), "*\n")

    def test_erase_cell_from_universe(self):
        universe_service = UniverseService(1, 1)
        universe_service.add_cell(0, 0)
        self.assertEqual(universe_service.get_textual_presentation(), "*\n")
        universe_service.erase_cell(0, 0)
        self.assertEqual(universe_service.get_textual_presentation(), ".\n")

    def test_add_cell_outside_universe(self):
        universe_service = UniverseService(1, 1)
        universe_service.add_cell(1, 1)
        self.assertEqual(universe_service.get_textual_presentation(), ".\n")

    def test_erase_cell_outside_universe(self):
        universe_service = UniverseService(1, 1)
        universe_service.add_cell(0, 0)
        self.assertEqual(universe_service.get_textual_presentation(), "*\n")
        universe_service.erase_cell(1, 1)
        self.assertEqual(universe_service.get_textual_presentation(), "*\n")

    def test_clear_universe(self):
        universe_service = UniverseService(1, 1)
        universe_service.add_cell(0, 0)
        self.assertEqual(universe_service.get_textual_presentation(), "*\n")
        universe_service.clear_universe()
        self.assertEqual(universe_service.get_textual_presentation(), ".\n")
