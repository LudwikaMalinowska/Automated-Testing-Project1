import unittest

from MorseCode.MorseCode import MorseCode


class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_morse_a_encode(self):
        self.assertEqual(self.temp.morse_encode("a"), "._")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()