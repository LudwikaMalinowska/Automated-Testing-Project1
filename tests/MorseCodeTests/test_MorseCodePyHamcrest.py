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
        assert_that(self.temp.morse_encode("a"), equal_to(".-"))

    def test_encode_a_length(self):
        assert_that(self.temp.morse_encode("a"), has_length(len(".-")))

    def test_encode_d_equal(self):
        assert_that(self.temp.morse_encode("d"), equal_to("-.."))

    def test_encode_d_not_none(self):
        assert_that(self.temp.morse_encode("d"), not_none())

    def test_encode_n_equal(self):
        assert_that(self.temp.morse_encode("n"), equal_to("-."))

    def test_encode_n_has_string(self):
        assert_that(self.temp.morse_encode("n"), has_string("-."))

    def test_encode_z_equal(self):
        assert_that(self.temp.morse_encode("z"), equal_to("--.."))

    def test_encode_z_contains_in_order(self):
        assert_that(self.temp.morse_encode("z"), string_contains_in_order("-", "-", "."))

    def test_decode_a_equal(self):
        assert_that(self.temp.morse_decode(".-"), equal_to("a"))

    def test_decode_a_starts_with(self):
        assert_that(self.temp.morse_decode(".-"), has_string(starts_with('a')))

    def test_decode_d_equal(self):
        assert_that(self.temp.morse_decode("-.."), equal_to("d"))

    def test_decode_d_starts_with(self):
        assert_that(self.temp.morse_decode("-.."), has_string(ends_with('d')))

    def test_decode_n_equal(self):
        assert_that(self.temp.morse_decode("-."), equal_to("n"))

    def test_decode_z_equal(self):
        assert_that(self.temp.morse_decode("--.."), equal_to("z"))

    def test_encode_abc_equal(self):
        assert_that(self.temp.morse_encode("abc"), equal_to(".- -... -.-."))

    def test_encode_xyz_equal(self):
        assert_that(self.temp.morse_encode("xyz"), equal_to("-..- -.-- --.."))

    def test_encode_123_equal(self):
        assert_that(self.temp.morse_encode("123"), equal_to(".---- ..--- ...--"))

    def test_encode_abc_def_equal(self):
        assert_that(self.temp.morse_encode("abc def"), equal_to(".- -... -.-.      -.. . ..-."))

    def test_encode_xyz_123_equal(self):
        assert_that(self.temp.morse_encode("xyz 123"), equal_to("-..- -.-- --..      .---- ..--- ...--"))

    def test_encode_veni_vidi_equal(self):
        assert_that(self.temp.morse_encode("veni vidi"), equal_to("...- . -. ..      ...- .. -.. .."))

    def test_encode_pangram_equal(self):
        assert_that(self.temp.morse_encode("the quick brown fox jumps over the lazy dog"),
                    equal_to(
                        "- .... .      --.- ..- .. -.-. -.-"
                        "      -... .-. --- .-- -.      ..-. --- -..-"
                        "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
                        "      .-.. .- --.. -.--      -.. --- --."
                    ))

    def test_encode_special_characters(self):
        special_chars = ",.?;:/-'" + '"' + "_()=+@"
        special_chars_morse = "--..-- .-.-.- ..--.. -.-.-. ---... -..-. -....- .----. .-..-. ..--.- "
        "-.--. -.--.- -...- .-.-. .--.-."
        assert_that(self.temp.morse_encode(special_chars), equal_to(special_chars_morse))

    def test_decode_abc_equal(self):
        assert_that(self.temp.morse_decode(".- -... -.-."), equal_to("abc"))

    def test_decode_xyz_equal(self):
        assert_that(self.temp.morse_decode("-..- -.-- --.."), equal_to("xyz"))

    def test_decode_123_equal(self):
        assert_that(self.temp.morse_decode(".---- ..--- ...--"), equal_to("123"))

    def test_decode_abc_def_equal(self):
        assert_that(self.temp.morse_decode(".- -... -.-.      -.. . ..-."), equal_to("abc def"))

    def test_decode_xyz_123_equal(self):
        assert_that(self.temp.morse_decode("-..- -.-- --..      .---- ..--- ...--"), equal_to("xyz 123"))

    def test_decode_veni_vidi_equal(self):
        assert_that(self.temp.morse_decode("...- . -. ..      ...- .. -.. .."), equal_to("veni vidi"))

    def test_decode_pangram_equal(self):
        assert_that(self.temp.morse_decode(
            "- .... .      --.- ..- .. -.-. -.-"
            "      -... .-. --- .-- -.      ..-. --- -..-"
            "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
            "      .-.. .- --.. -.--      -.. --- --."
        ),
                    equal_to("the quick brown fox jumps over the lazy dog"))

    def test_encode_exception1(self):
        assert_that(calling(self.temp.morse_encode).with_args(1), raises(ValueError))

    def test_encode_exception2(self):
        assert_that(calling(self.temp.morse_encode).with_args(None), raises(ValueError))

    def test_encode_exception3(self):
        assert_that(calling(self.temp.morse_encode).with_args("ą"), raises(ValueError))

    def test_decode_exception1(self):
        assert_that(calling(self.temp.morse_decode).with_args(1), raises(ValueError))

    def test_decode_exception2(self):
        assert_that(calling(self.temp.morse_decode).with_args(None), raises(ValueError))

    def test_decode_exception3(self):
        assert_that(calling(self.temp.morse_decode).with_args("ą"), raises(ValueError))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()