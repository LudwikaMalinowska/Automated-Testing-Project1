import unittest
from AffineCipher.AffineCipher import AffineCipher
from assertpy import assert_that


class AffineTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_cipher_a(self):
        assert_that(self.temp.affine_cipher("a", 1, 3)).is_equal_to("d")

    def test_cipher_z(self):
        assert_that(self.temp.affine_cipher("z", 1, 3)).is_equal_to("c")

    def test_cipher_abc(self):
        assert_that(self.temp.affine_cipher("abc", 3, 12)).is_equal_to("mps")

    def test_cipher_veni_vidi(self):
        assert_that(self.temp.affine_cipher("veni vidi", 3, 12)).is_equal_to("xyzk xkvk")

    def test_cipher_pangram(self):
        assert_that(self.temp.affine_cipher("the quick brown fox jumps over the lazy dog", 3, 12))\
            .is_equal_to("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce")

    def test_decipher_a(self):
        assert_that(self.temp.affine_decipher("d", 1, 3)).is_equal_to("a")

    def test_decipher_z(self):
        assert_that(self.temp.affine_decipher("c", 1, 3)).is_equal_to("z")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
