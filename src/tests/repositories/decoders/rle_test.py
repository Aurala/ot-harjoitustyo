import unittest
from repositories.decoders.rle import RLE


class TestRLE(unittest.TestCase):

    def setUp(self):
        self.decoder = RLE()
        self.valid_RLE = ["#N Blinker\n",
                          "#C Valid RLE file for unit testing\n",
                          "x = 3, y = 1, rule = B3/S23\n",
                          "3o!\n"]
        self.invalid_RLE = ["#N Blinker\n",
                            "#C Valid RLE file for unit testing\n",
                            "x = 3, y = 1, rule = b3/s23\n",
                            "3o!\n"]

    def test_can_decode_valid_RLE(self):
        name, rules, pattern, metadata = self.decoder.decode(self.valid_RLE)
        self.assertEqual(name, "Blinker")
        self.assertEqual(rules, "B3/S23")
        self.assertEqual(pattern, [[1, 1, 1]])
        self.assertEqual(
            metadata, "#N Blinker\n#C Valid RLE file for unit testing\n")
        
    def test_can_decode_invalid_RLE_with_lowercase(self):
        name, rules, pattern, metadata = self.decoder.decode(self.valid_RLE)
        self.assertEqual(name, "Blinker")
        self.assertEqual(rules, "B3/S23")
        self.assertEqual(pattern, [[1, 1, 1]])
        self.assertEqual(
            metadata, "#N Blinker\n#C Valid RLE file for unit testing\n")
