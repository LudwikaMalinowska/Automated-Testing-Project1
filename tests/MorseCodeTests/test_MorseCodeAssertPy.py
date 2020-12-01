import unittest
from MorseCode.MorseCode import MorseCode
from assertpy import assert_that

class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_MorseCode_Instance(self):
        assert_that(self.temp).is_instance_of(MorseCode)

    def test_encode_a(self):
        assert_that(self.temp.morse_encode("a")).is_equal_to("._")

    def test_encode_a_starts_with(self):
        assert_that(self.temp.morse_encode("a")).starts_with('.')

    def test_encode_d(self):
        assert_that(self.temp.morse_encode("d")).is_equal_to("_..")

    def test_encode_d_ends_with(self):
        assert_that(self.temp.morse_encode("d")).ends_with(".")

    def test_encode_n(self):
        assert_that(self.temp.morse_encode("n")).is_equal_to("_.")

    def test_encode_n_starts_with_ends_with(self):
        assert_that(self.temp.morse_encode("n")).starts_with('_').ends_with('.')

    def test_encode_z(self):
        assert_that(self.temp.morse_encode("z")).is_equal_to("__..")

    def test_encode_z_contains(self):
        assert_that(self.temp.morse_encode("z")).contains(".")

    def test_decode_a(self):
        assert_that(self.temp.morse_decode("._")).is_equal_to("a")

    def test_decode_a_doesnt_contain(self):
        assert_that(self.temp.morse_decode("._")).does_not_contain("b")

    def test_decode_d(self):
        assert_that(self.temp.morse_decode("_..")).is_equal_to("d")

    def test_decode_d_contain_doesnt_contain(self):
        assert_that(self.temp.morse_decode("_..")).contains("d").does_not_contain("c")

    def test_decode_n(self):
        assert_that(self.temp.morse_decode("_.")).is_equal_to("n")

    def test_decode_z(self):
        assert_that(self.temp.morse_decode("__..")).is_equal_to("z")

    def test_encode_abc(self):
        assert_that(self.temp.morse_encode("abc")).is_equal_to("._ _... _._.")

    def test_encode_xyz(self):
        assert_that(self.temp.morse_encode("xyz")).is_equal_to("_.._ _.__ __..")

    def test_encode_123(self):
        assert_that(self.temp.morse_encode("123")).is_equal_to(".____ ..___ ...__")

    def test_encode_abc_def(self):
        assert_that(self.temp.morse_encode("abc def")).is_equal_to("._ _... _._.      _.. . .._.")

    def test_encode_xyz_123(self):
        assert_that(self.temp.morse_encode("xyz 123")).is_equal_to("_.._ _.__ __..      .____ ..___ ...__")

    def test_encode_veni_vidi(self):
        assert_that(self.temp.morse_encode("veni vidi")).is_equal_to("..._ . _. ..      ..._ .. _.. ..")

    def test_decode_abc(self):
        assert_that(self.temp.morse_decode("._ _... _._.")).is_equal_to("abc")

    def test_decode_xyz(self):
        assert_that(self.temp.morse_decode("_.._ _.__ __..")).is_equal_to("xyz")

    def test_decode_123(self):
        assert_that(self.temp.morse_decode(".____ ..___ ...__")).is_equal_to("123")

    def test_decode_abc_def(self):
        assert_that(self.temp.morse_decode("._ _... _._.      _.. . .._.")).is_equal_to("abc def")

    def test_decode_xyz_123(self):
        assert_that(self.temp.morse_decode("_.._ _.__ __..      .____ ..___ ...__")).is_equal_to("xyz 123")

    def test_decode_veni_vidi(self):
        assert_that(self.temp.morse_decode("..._ . _. ..      ..._ .. _.. ..")).is_equal_to("veni vidi")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
