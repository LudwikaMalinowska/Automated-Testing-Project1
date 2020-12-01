import unittest
from CaesarCipher.CaesarCipher import CaesarCipher
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class CaesarParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = CaesarCipher()

    @parameterized.expand([
        ("d", "a"),
    ])
    def test_one_parameterized(self, text, result):
        self.assertEqual(self.tmp.caesar_decipher(text), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("d", "a"),
])
def test_morse_encode_outside_class(text, result):
    r = CaesarCipher()
    assert_equal(r.caesar_decipher(text), result)


@parameterized_class(('text', 'result'), [
    ("d", "a"),
])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = CaesarCipher()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.caesar_decipher(self.text), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()