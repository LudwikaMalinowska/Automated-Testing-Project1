import unittest
from AffineCipher.AffineCipher import AffineCipher
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher


class AffineTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_encode_a_equal(self):
        assert_that(self.temp.affine_cipher("a", 1, 3), equal_to("d"))

    def test_encode_z_equal(self):
        assert_that(self.temp.affine_cipher("z", 1, 3), equal_to("c"))

    def test_encode_abc_equal(self):
        assert_that(self.temp.affine_cipher("abc", 3, 12), equal_to("mps"))

    def test_encode_veni_vidi_equal(self):
        assert_that(self.temp.affine_cipher("veni vidi", 3, 12), equal_to("xyzk xkvk"))

    def test_encode_pangram_equal(self):
        assert_that(self.temp.affine_cipher("the quick brown fox jumps over the lazy dog", 3, 12),
                    equal_to("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce"))

    def test_decipher_a_equal(self):
        assert_that(self.temp.affine_cipher("d", 1, 3), equal_to("a"))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
