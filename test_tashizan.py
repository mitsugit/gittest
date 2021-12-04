# comment by Kei
import unittest
from tashizan import tashizan

class TestTashizan(unittest.TestCase):
        def test_tashizan(self):

            value1 = 2
            value2 = 6
            expected = 8
            actual = tashizan(value1, value2)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()