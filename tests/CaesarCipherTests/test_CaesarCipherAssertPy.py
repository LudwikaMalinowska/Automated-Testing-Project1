import unittest
from CaesarCipher.CaesarCipher import CaesarCipher
from assertpy import assert_that


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = CaesarCipher()

    def test_Caesar_Instance(self):
        assert_that(self.temp).is_instance_of(CaesarCipher)

    def test_encode_a(self):
        assert_that(self.temp.caesar_cipher("a")).is_equal_to("d")

    def test_encode_w(self):
        assert_that(self.temp.caesar_cipher("w")).is_equal_to("z")

    def test_encode_x(self):
        assert_that(self.temp.caesar_cipher("x")).is_equal_to("a")

    def test_encode_z(self):
        assert_that(self.temp.caesar_cipher("z")).is_equal_to("c")

    def test_encode_abc(self):
        assert_that(self.temp.caesar_cipher("abc")).is_equal_to("def")

    def test_encode_wxyz(self):
        assert_that(self.temp.caesar_cipher("wxyz")).is_equal_to("zabc")

    def test_encode_veni(self):
        assert_that(self.temp.caesar_cipher("veni")).is_equal_to("yhql")

    def test_encode_abc_def(self):
        assert_that(self.temp.caesar_cipher("abc def")).is_equal_to("def ghi")

    def test_encode_veni_vidi_vici(self):
        assert_that(self.temp.caesar_cipher("veni vidi vici")).is_equal_to("yhql ylgl ylfl")

    def test_encode_pangram(self):
        assert_that(self.temp.caesar_cipher("the quick brown fox jumps over the lazy dog"))\
            .is_equal_to("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")

    def test_decode_a(self):
        assert_that(self.temp.caesar_decipher("d")).is_equal_to("a")

    def test_decode_w(self):
        assert_that(self.temp.caesar_decipher("z")).is_equal_to("w")

    def test_decode_x(self):
        assert_that(self.temp.caesar_decipher("a")).is_equal_to("x")

    def test_decode_z(self):
        assert_that(self.temp.caesar_decipher("c")).is_equal_to("z")

    def test_decode_abc(self):
        assert_that(self.temp.caesar_decipher("def")).is_equal_to("abc")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
