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

    def test_abc_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("abc"), "def")

    def test_wxyz_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("wxyz"), "zabc")

    def test_veni_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("veni"), "yhql")

    def test_abc_def_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("abc def"), "def ghi")

    def test_veni_vidi_vici_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("veni vidi vici"), "yhql ylgl ylfl")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()