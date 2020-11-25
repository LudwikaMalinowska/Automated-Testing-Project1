import unittest

from MorseCode.MorseCode import MorseCode


class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_morse_a_encode(self):
        self.assertEqual(self.temp.morse_encode("a"), "._")

    def test_morse_d_encode(self):
        self.assertEqual(self.temp.morse_encode("d"), "_..")

    def test_morse_n_encode(self):
        self.assertEqual(self.temp.morse_encode("n"), "_.")

    def test_morse_z_encode(self):
        self.assertEqual(self.temp.morse_encode("z"), "__..")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()