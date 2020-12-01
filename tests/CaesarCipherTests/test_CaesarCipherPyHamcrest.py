import unittest
from CaesarCipher.CaesarCipher import CaesarCipher
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = CaesarCipher()

    def test_Caesar_Instance(self):
        assert_that(self.temp, instance_of(CaesarCipher))

    def test_encode_a_equal(self):
        assert_that(self.temp.caesar_cipher("a"), equal_to("d"))

    def test_encode_w_equal(self):
        assert_that(self.temp.caesar_cipher("w"), equal_to("z"))

    def test_encode_x_equal(self):
        assert_that(self.temp.caesar_cipher("x"), equal_to("a"))

    def test_encode_z_equal(self):
        assert_that(self.temp.caesar_cipher("z"), equal_to("c"))

    def test_encode_abc_equal(self):
        assert_that(self.temp.caesar_cipher("abc"), equal_to("def"))

    def test_encode_wxyz_equal(self):
        assert_that(self.temp.caesar_cipher("wxyz"), equal_to("zabc"))

    def test_encode_veni_equal(self):
        assert_that(self.temp.caesar_cipher("veni"), equal_to("yhql"))

    def test_encode_abc_def_equal(self):
        assert_that(self.temp.caesar_cipher("abc def"), equal_to("def ghi"))

    def test_encode_veni_vidi_vici_equal(self):
        assert_that(self.temp.caesar_cipher("veni vidi vici"), equal_to("yhql ylgl ylfl"))

    def test_decode_a_equal(self):
        assert_that(self.temp.caesar_decipher("d"), equal_to("a"))

    def test_decode_z_equal(self):
        assert_that(self.temp.caesar_decipher("z"), equal_to("w"))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()