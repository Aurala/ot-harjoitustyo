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

    def test_returns_the_height(self):
        self.assertEqual(self.universe.true_height, 15)
        self.assertEqual(self.universe.height, 5)

    def test_returns_the_width(self):
        self.assertEqual(self.universe.true_width, 15)
        self.assertEqual(self.universe.width, 5)
