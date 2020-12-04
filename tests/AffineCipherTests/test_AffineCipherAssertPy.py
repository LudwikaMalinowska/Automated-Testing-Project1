import unittest
from AffineCipher.AffineCipher import AffineCipher
from assertpy import assert_that


class AffineTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_cipher_a(self):
        assert_that(self.temp.caesar_cipher("a", 1, 3)).is_equal_to("d")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
