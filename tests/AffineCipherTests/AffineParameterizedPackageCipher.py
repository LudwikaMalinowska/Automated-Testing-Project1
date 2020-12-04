import unittest
from AffineCipher.AffineCipher import AffineCipher
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class CaesarParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = AffineCipher()

    @parameterized.expand([
        ("a", 1, 3, "d"),
    ])
    def test_one_parameterized(self, text, a, b, result):
        self.assertEqual(self.tmp.affine_cipher(text, a, b), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("a", 1, 3, "d"),
])
def test_morse_encode_outside_class(text, a, b, result):
    r = AffineCipher()
    assert_equal(r.affine_cipher(text, a, b), result)


@parameterized_class(('text', 'a', 'b', 'result'), [
    ("a", 1, 3, "d"),
])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = AffineCipher()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.affine_cipher(self.text, self.a, self.b), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()