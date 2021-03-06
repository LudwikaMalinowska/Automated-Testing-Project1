import unittest
from CaesarCipher.CaesarCipher import CaesarCipher
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class CaesarParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = CaesarCipher()

    @parameterized.expand([
        ("a", "d"),
        ("w", "z"),
        ("x", "a"),
        ("z", "c"),
        ("abc", "def"),
        ("wxyz", "zabc"),
        ("veni", "yhql"),
        ("abc def", "def ghi"),
        ("veni vidi vici", "yhql ylgl ylfl"),
        ("the quick brown fox jumps over the lazy dog",
         "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")
    ])
    def test_one_parameterized(self, text, result):
        self.assertEqual(self.tmp.caesar_cipher(text), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("a", "d"),
    ("w", "z"),
    ("x", "a"),
    ("z", "c"),
    ("abc", "def"),
    ("wxyz", "zabc"),
    ("veni", "yhql"),
    ("abc def", "def ghi"),
    ("veni vidi vici", "yhql ylgl ylfl"),
    ("the quick brown fox jumps over the lazy dog",
     "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")
])
def test_morse_encode_outside_class(text, result):
    r = CaesarCipher()
    assert_equal(r.caesar_cipher(text), result)


@parameterized_class(('text', 'result'), [
    ("a", "d"),
    ("w", "z"),
    ("x", "a"),
    ("z", "c"),
    ("abc", "def"),
    ("wxyz", "zabc"),
    ("veni", "yhql"),
    ("abc def", "def ghi"),
    ("veni vidi vici", "yhql ylgl ylfl"),
    ("the quick brown fox jumps over the lazy dog",
     "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")
])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = CaesarCipher()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.caesar_cipher(self.text), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()