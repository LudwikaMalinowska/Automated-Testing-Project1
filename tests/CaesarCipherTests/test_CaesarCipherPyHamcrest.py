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

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()