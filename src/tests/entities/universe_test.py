import unittest
import numpy as np
from entities.universe import Universe


class TestUniverse(unittest.TestCase):

    def setUp(self):
        self.universe = Universe()

    def test_returns_visible_universe_as_python_list(self):
        universe = self.universe.get_universe_as_list()
        self.assertEqual(isinstance(universe, list), True)
        self.assertEqual(len(universe[0]), 5)
        self.assertEqual(len(universe[1]), 5)

    def test_returns_visible_universe_as_numpy_array(self):
        universe = self.universe.get_universe_as_rgb_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        self.assertEqual(universe.shape, (5, 5, 3))

    def test_returns_entire_universe_as_numpy_array(self):
        universe = self.universe.get_entire_universe_as_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        self.assertEqual(universe.shape, (15, 15))

    def test_returns_height(self):
        self.assertEqual(self.universe.height, 5)

    def test_returns_width(self):
        self.assertEqual(self.universe.width, 5)

    def test_returns_true_height(self):
        self.assertEqual(self.universe.true_height, 15)

    def test_returns_true_width(self):
        self.assertEqual(self.universe.true_width, 15)

    def test_counts_cells(self):
        self.assertEqual(self.universe.count_cells(), 0)

    def test_inverts_cell(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.invert_cell(1, 1)
        self.assertEqual(self.universe.count_cells(), 1)

    def test_inverts_cell_outside_universe(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.invert_cell(42, 42)
        self.assertEqual(self.universe.count_cells(), 0)

    def test_adds_cell(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.add_cell(1, 1)
        self.assertEqual(self.universe.count_cells(), 1)

    def test_adds_cell_outside_universe(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.add_cell(42, 42)
        self.assertEqual(self.universe.count_cells(), 0)

    def test_erases_cell(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.add_cell(1, 1)
        self.assertEqual(self.universe.count_cells(), 1)
        self.universe.erase_cell(1, 1)
        self.assertEqual(self.universe.count_cells(), 0)

    def test_erases_cell_outside_universe(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.add_cell(42, 42)
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.erase_cell(42, 42)
        self.assertEqual(self.universe.count_cells(), 0)

    def test_clears_universe(self):
        self.assertEqual(self.universe.count_cells(), 0)
        self.universe.add_cell(1, 1)
        self.assertEqual(self.universe.count_cells(), 1)
        self.universe.clear_universe()
        self.assertEqual(self.universe.count_cells(), 0)

    def test_increases_size(self):
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)
        self.universe.change_size(100)
        self.assertEqual(self.universe.width, 105)
        self.assertEqual(self.universe.height, 105)

    def test_decreases_size(self):
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)
        self.universe.change_size(-4)
        self.assertEqual(self.universe.width, 1)
        self.assertEqual(self.universe.height, 1)

    def test_does_not_change_size_to_zero(self):
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)
        self.universe.change_size(-5)
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)

    def test_does_not_change_size_to_negative(self):
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)
        self.universe.change_size(-6)
        self.assertEqual(self.universe.width, 5)
        self.assertEqual(self.universe.height, 5)
