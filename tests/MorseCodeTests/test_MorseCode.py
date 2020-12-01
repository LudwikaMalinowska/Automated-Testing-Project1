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

    def test_morse_abc_decode(self):
        self.assertEqual(self.temp.morse_decode("._ _... _._."), "abc")

    def test_morse_xyz_decode(self):
        self.assertEqual(self.temp.morse_decode("_.._ _.__ __.."), "xyz")

    def test_morse_123_decode(self):
        self.assertEqual(self.temp.morse_decode(".____ ..___ ...__"), "123")

    def test_morse_abc_def_decode(self):
        self.assertEqual(self.temp.morse_decode("._ _... _._.      _.. . .._."), "abc def")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()