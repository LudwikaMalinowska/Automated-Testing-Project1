import unittest
from MorseCode.MorseCode import MorseCode
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher


class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_MorseCode_Instance(self):
        assert_that(self.temp, instance_of(MorseCode))

    def test_encode_a_equal(self):
        assert_that(self.temp.morse_encode("a"), equal_to("._"))

    def test_encode_a_length(self):
        assert_that(self.temp.morse_encode("a"), has_length(len("._")))

    def test_encode_d_equal(self):
        assert_that(self.temp.morse_encode("d"), equal_to("_.."))

    def test_encode_d_not_none(self):
        assert_that(self.temp.morse_encode("d"), not_none())

    def test_encode_n_equal(self):
        assert_that(self.temp.morse_encode("n"), equal_to("_."))

    def test_encode_n_has_string(self):
        assert_that(self.temp.morse_encode("n"), has_string("_."))

    def test_encode_z_equal(self):
        assert_that(self.temp.morse_encode("z"), equal_to("__.."))

    def test_encode_z_contains_in_order(self):
        assert_that(self.temp.morse_encode("z"), string_contains_in_order("_", "_", "."))

    def test_decode_a_equal(self):
        assert_that(self.temp.morse_decode("._"), equal_to("a"))

    def test_decode_a_starts_with(self):
        assert_that(self.temp.morse_decode("._"), has_string(starts_with('a')))

    def test_decode_d_equal(self):
        assert_that(self.temp.morse_decode("_.."), equal_to("d"))

    def test_decode_d_starts_with(self):
        assert_that(self.temp.morse_decode("_.."), has_string(ends_with('d')))

    def test_decode_n_equal(self):
        assert_that(self.temp.morse_decode("_."), equal_to("n"))

    def test_decode_z_equal(self):
        assert_that(self.temp.morse_decode("__.."), equal_to("z"))

    def test_encode_abc_equal(self):
        assert_that(self.temp.morse_encode("abc"), equal_to("._ _... _._."))

    def test_encode_xyz_equal(self):
        assert_that(self.temp.morse_encode("xyz"), equal_to("_.._ _.__ __.."))

    def test_encode_123_equal(self):
        assert_that(self.temp.morse_encode("123"), equal_to(".____ ..___ ...__"))

    def test_encode_abc_def_equal(self):
        assert_that(self.temp.morse_encode("abc def"), equal_to("._ _... _._.      _.. . .._."))

    def test_encode_xyz_123_equal(self):
        assert_that(self.temp.morse_encode("xyz 123"), equal_to("_.._ _.__ __..      .____ ..___ ...__"))

    def test_encode_veni_vidi_equal(self):
        assert_that(self.temp.morse_encode("veni vidi"), equal_to("..._ . _. ..      ..._ .. _.. .."))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()