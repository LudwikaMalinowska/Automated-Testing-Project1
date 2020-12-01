import unittest

from CaesarCipher.CaesarCipher import CaesarCipher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = CaesarCipher()

    def test_a_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("a"), "d")

    def test_w_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("w"), "z")

    def test_x_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("x"), "a")

    def test_z_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("z"), "c")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()