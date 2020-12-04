import unittest

from MorseCode.MorseCode import MorseCode


class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_morse_a_encode(self):
        self.assertEqual(self.temp.morse_encode("a"), "._")

    def test_morse_d_encode(self):
        self.assertEqual(self.temp.morse_encode("d"), "_..")

    def test_morse_n_encode(self):
        self.assertEqual(self.temp.morse_encode("n"), "_.")

    def test_morse_z_encode(self):
        self.assertEqual(self.temp.morse_encode("z"), "__..")

    def test_morse_a_decode(self):
        self.assertEqual(self.temp.morse_decode("._"), "a")

    def test_morse_d_decode(self):
        self.assertEqual(self.temp.morse_decode("_.."), "d")

    def test_morse_n_decode(self):
        self.assertEqual(self.temp.morse_decode("_."), "n")

    def test_morse_z_decode(self):
        self.assertEqual(self.temp.morse_decode("__.."), "z")

    def test_morse_abc_encode(self):
        self.assertEqual(self.temp.morse_encode("abc"), "._ _... _._.")

    def test_morse_xyz_encode(self):
        self.assertEqual(self.temp.morse_encode("xyz"), "_.._ _.__ __..")

    def test_morse_123_encode(self):
        self.assertEqual(self.temp.morse_encode("123"), ".____ ..___ ...__")

    def test_morse_abc_def_encode(self):
        self.assertEqual(self.temp.morse_encode("abc def"), "._ _... _._.      _.. . .._.")

    def test_morse_xyz_123_encode(self):
        self.assertEqual(self.temp.morse_encode("xyz 123"), "_.._ _.__ __..      .____ ..___ ...__")

    def test_morse_veni_vidi_encode(self):
        self.assertEqual(self.temp.morse_encode("veni vidi"), "..._ . _. ..      ..._ .. _.. ..")

    def test_morse_pangram_encode(self):
        self.assertEqual(self.temp.morse_encode("the quick brown fox jumps over the lazy dog"),
                         "_ .... .      __._ .._ .. _._. _._      _... ._. ___ .__ _.      .._. ___ _.._      .___ .._ __ .__. ...      ___ ..._ . ._.      _ .... .      ._.. ._ __.. _.__      _.. ___ __.")

    def test_morse_abc_decode(self):
        self.assertEqual(self.temp.morse_decode("._ _... _._."), "abc")

    def test_morse_xyz_decode(self):
        self.assertEqual(self.temp.morse_decode("_.._ _.__ __.."), "xyz")

    def test_morse_123_decode(self):
        self.assertEqual(self.temp.morse_decode(".____ ..___ ...__"), "123")

    def test_morse_abc_def_decode(self):
        self.assertEqual(self.temp.morse_decode("._ _... _._.      _.. . .._."), "abc def")

    def test_morse_xyz_123_decode(self):
        self.assertEqual(self.temp.morse_decode("_.._ _.__ __..      .____ ..___ ...__"), "xyz 123")

    def test_morse_veni_vidi_decode(self):
        self.assertEqual(self.temp.morse_decode("..._ . _. ..      ..._ .. _.. .."), "veni vidi")

    def test_morse_pangram_decode(self):
        self.assertEqual(self.temp.morse_decode("_ .... .      __._ .._ .. _._. _._      _... ._. ___ .__ _.      .._. ___ _.._      .___ .._ __ .__. ...      ___ ..._ . ._.      _ .... .      ._.. ._ __.. _.__      _.. ___ __."),
                         "the quick brown fox jumps over the lazy dog")

    def test_morse_encode_raises1(self):
        self.assertRaises(ValueError, self.temp.morse_encode, 1)

    def test_morse_encode_raises2(self):
        self.assertRaises(ValueError, self.temp.morse_encode, None)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()