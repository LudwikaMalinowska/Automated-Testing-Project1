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

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
