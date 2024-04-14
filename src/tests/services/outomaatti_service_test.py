import unittest
from services.outomaatti_service import OutomaattiService


class TestOutomaattiService(unittest.TestCase):

    blinker_vertical = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    blinker_horizontal = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

    def setUp(self):
        self.outomaatti = OutomaattiService()

    def test_create_service_with_default_parameters(self):
        self.assertEqual(self.outomaatti.get_universe_as_text(),
                         ".....\n.....\n.....\n.....\n.....\n")

    def test_create_service_with_universe_of_4x5(self):
        outomaatti = OutomaattiService(4, 5)
        self.assertEqual(outomaatti.get_universe_as_text(),
                         "....\n....\n....\n....\n....\n")

    def test_universe_dimensions(self):
        outomaatti = OutomaattiService(42, 69)
        self.assertEqual(outomaatti.get_width(), 42)
        self.assertEqual(outomaatti.get_height(), 69)

    def test_add_cell_to_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")

    def test_add_patterns_to_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        self.assertEqual(outomaatti.get_universe_as_text(), ".*.\n.*.\n.*.\n")
        outomaatti.add_pattern(0, 0, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), ".*.\n***\n.*.\n")

    def test_add_patterns_partly_outside_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(2, 1, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n...\n..*\n")

    def test_add_patterns_completely_outside_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(10, 10, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n...\n...\n")

    def test_simulate_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        outomaatti.next_generation()
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n***\n...\n")

    def test_count_cells_in_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        self.assertEqual(outomaatti.count_cells(), 3)

    def test_erase_cell_from_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")
        outomaatti.erase_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")

    def test_add_cell_outside_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(1, 1)
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")

    def test_erase_cell_outside_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")
        outomaatti.erase_cell(1, 1)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")

    def test_clear_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")
        outomaatti.clear_universe()
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")
