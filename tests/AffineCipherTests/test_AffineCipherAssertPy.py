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

    def test_decipher_abc(self):
        assert_that(self.temp.affine_decipher("mps", 3, 12)).is_equal_to("abc")

    def test_decipher_veni(self):
        assert_that(self.temp.affine_decipher("xyzk", 3, 12)).is_equal_to("veni")

    def test_decipher_veni_vidi(self):
        assert_that(self.temp.affine_decipher("xyzk xkvk", 3, 12)).is_equal_to("veni vidi")

    def test_decipher_pangram(self):
        assert_that(self.temp.affine_decipher("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce", 3, 12))\
            .is_equal_to("the quick brown fox jumps over the lazy dog")

    def test_encode_exception1(self):
        assert_that(self.temp.affine_cipher).raises(ValueError).when_called_with(1, 1, 3)

    def test_encode_exception2(self):
        assert_that(self.temp.affine_cipher).raises(ValueError).when_called_with(None, 1, 3)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
