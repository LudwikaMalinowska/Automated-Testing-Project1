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

    def test_encode_pangram_equal(self):
        assert_that(self.temp.caesar_cipher("the quick brown fox jumps over the lazy dog"),
                    equal_to("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"))

    def test_decode_a_equal(self):
        assert_that(self.temp.caesar_decipher("d"), equal_to("a"))

    def test_decode_w_equal(self):
        assert_that(self.temp.caesar_decipher("z"), equal_to("w"))

    def test_decode_x_equal(self):
        assert_that(self.temp.caesar_decipher("a"), equal_to("x"))

    def test_decode_z_equal(self):
        assert_that(self.temp.caesar_decipher("c"), equal_to("z"))

    def test_decode_abc_equal(self):
        assert_that(self.temp.caesar_decipher("def"), equal_to("abc"))

    def test_decode_wxyz_equal(self):
        assert_that(self.temp.caesar_decipher("zabc"), equal_to("wxyz"))

    def test_decode_veni_equal(self):
        assert_that(self.temp.caesar_decipher("yhql"), equal_to("veni"))

    def test_decode_abc_def_equal(self):
        assert_that(self.temp.caesar_decipher("def ghi"), equal_to("abc def"))

    def test_decode_veni_vidi_vici_equal(self):
        assert_that(self.temp.caesar_decipher("yhql ylgl ylfl"), equal_to("veni vidi vici"))

    def test_decode_pangram_equal(self):
        assert_that(self.temp.caesar_decipher("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"),
                    equal_to("the quick brown fox jumps over the lazy dog"))

    def test_encode_exception1(self):
        assert_that(calling(self.temp.caesar_cipher).with_args(1), raises(ValueError))

    def test_encode_exception2(self):
        assert_that(calling(self.temp.caesar_cipher).with_args(None), raises(ValueError))

    def test_decode_exception1(self):
        assert_that(calling(self.temp.caesar_decipher).with_args(1), raises(ValueError))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()