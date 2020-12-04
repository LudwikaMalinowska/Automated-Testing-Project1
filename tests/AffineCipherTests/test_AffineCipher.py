import unittest

from AffineCipher.AffineCipher import AffineCipher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_a_cipher(self):
        self.assertEqual(self.temp.affine_cipher("a", 1, 3), "d")

    def test_z_cipher(self):
        self.assertEqual(self.temp.affine_cipher("z", 1, 3), "c")

    def test_abc_cipher(self):
        self.assertEqual(self.temp.affine_cipher("abc", 3, 12), "mps")

    def test_veni_vidi_cipher(self):
        self.assertEqual(self.temp.affine_cipher("veni vidi", 3, 12), "xyzk xkvk")

    def test_pangram_cipher(self):
        self.assertEqual(self.temp.affine_cipher("the quick brown fox jumps over the lazy dog", 3, 12),
                         "rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce")

    def test_a_decipher(self):
        self.assertEqual(self.temp.affine_decipher("d", 1, 3), "a")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
