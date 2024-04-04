import unittest
import numpy as np
from entities.universe import Universe

class TestUniverse(unittest.TestCase):

    def setUp(self):
        self.universe = Universe()

    def test_returns_python_list(self):
        universe = self.universe.get_universe_as_list()
        self.assertEqual(isinstance(universe, list), True)
        # Test size
        # Test contents

    def test_returns_numpy_array(self):
        universe = self.universe.get_universe_as_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        # Test size

    def test_returns_numpy_array(self):
        universe = self.universe.get_entire_universe_as_ndarray()
        self.assertEqual(isinstance(universe, np.ndarray), True)
        # Test size
