import unittest

from AffineCipher.AffineCipher import AffineCipher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_a_cipher(self):
        self.assertEqual(self.temp.affine_cipher("a", 1, 3), "d")

    def test_z_cipher(self):
        self.assertEqual(self.temp.affine_cipher("z", 1, 3), "c")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
