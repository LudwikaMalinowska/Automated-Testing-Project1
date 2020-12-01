import unittest
from MorseCode.MorseCode import MorseCode
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class MorseCodeParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    @parameterized.expand([
        ("._", "a"),
        ("_..", "d"),
        ("_.", "n"),
        ("__..", "z"),
        ("._ _... _._.", "abc"),
        ("_.._ _.__ __..", "xyz"),
        (".____ ..___ ...__", "123"),
        ("._ _... _._.      _.. . .._.", "abc def"),
        ("_.._ _.__ __..      .____ ..___ ...__", "xyz 123"),
        ("..._ . _. ..      ..._ .. _.. ..", "veni vidi"),
    ])
    def test_one_parameterized(self, text, result):
        self.assertEqual(self.tmp.morse_decode(text), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("._", "a"),
    ("_..", "d"),
    ("_.", "n"),
    ("__..", "z"),
    ("._ _... _._.", "abc"),
    ("_.._ _.__ __..", "xyz"),
    (".____ ..___ ...__", "123"),
    ("._ _... _._.      _.. . .._.", "abc def"),
    ("_.._ _.__ __..      .____ ..___ ...__", "xyz 123"),
    ("..._ . _. ..      ..._ .. _.. ..", "veni vidi"),
])
def test_morse_encode_outside_class(text, result):
    r = MorseCode()
    assert_equal(r.morse_decode(text), result)


@parameterized_class(('text', 'result'), [
    ("._", "a"),
    ("_..", "d"),
    ("_.", "n"),
    ("__..", "z"),
    ("._ _... _._.", "abc"),
    ("_.._ _.__ __..", "xyz"),
    (".____ ..___ ...__", "123"),
    ("._ _... _._.      _.. . .._.", "abc def"),
    ("_.._ _.__ __..      .____ ..___ ...__", "xyz 123"),
    ("..._ . _. ..      ..._ .. _.. ..", "veni vidi"),
])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.morse_decode(self.text), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
