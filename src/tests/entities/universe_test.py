import unittest
import numpy as np
from entities.universe import Universe


class TestUniverse(unittest.TestCase):

    def setUp(self):
        self.universe = Universe()

    def test_returns_python_list(self):
        universe = self.universe.get_universe_as_list()
        self.assertEqual(isinstance(universe, list), True)
        self.assertEqual(len(universe[0]), 5)
        self.assertEqual(len(universe[1]), 5)

    def test_returns_numpy_array(self):
        universe = self.universe.get_universe_as_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        self.assertEqual(universe.shape, (5, 5))

    def test_returns_numpy_array(self):
        universe = self.universe.get_entire_universe_as_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        self.assertEqual(universe.shape, (15, 15))
