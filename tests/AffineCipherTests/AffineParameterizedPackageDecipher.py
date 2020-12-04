import unittest
from AffineCipher.AffineCipher import AffineCipher
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class AffineParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = AffineCipher()

    @parameterized.expand([
        ("d", 1, 3, "a"),
        ("c", 1, 3, "z"),
        ("mps", 3, 12, "abc"),
        ("xyzk", 3, 12, "veni"),
        ("xyzk xkvk", 3, 12, "veni vidi"),
    ])
    def test_one_parameterized(self, text, a, b, result):
        self.assertEqual(self.tmp.affine_decipher(text, a, b), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("d", 1, 3, "a"),
    ("c", 1, 3, "z"),
    ("mps", 3, 12, "abc"),
    ("xyzk", 3, 12, "veni"),
    ("xyzk xkvk", 3, 12, "veni vidi"),
])
def test_affine_encode_outside_class(text, a, b, result):
    r = AffineCipher()
    assert_equal(r.affine_decipher(text, a, b), result)


@parameterized_class(('text', 'a', 'b', 'result'), [
    ("d", 1, 3, "a"),
    ("c", 1, 3, "z"),
    ("mps", 3, 12, "abc"),
    ("xyzk", 3, 12, "veni"),
    ("xyzk xkvk", 3, 12, "veni vidi"),
])
class AffineParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = AffineCipher()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.affine_decipher(self.text, self.a, self.b), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
