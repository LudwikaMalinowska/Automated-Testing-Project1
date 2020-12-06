import unittest

from MorseCode.MorseCode import MorseCode


class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_morse_a_encode(self):
        self.assertEqual(self.temp.morse_encode("a"), ".-")

    def test_morse_d_encode(self):
        self.assertEqual(self.temp.morse_encode("d"), "-..")

    def test_morse_n_encode(self):
        self.assertEqual(self.temp.morse_encode("n"), "-.")

    def test_morse_z_encode(self):
        self.assertEqual(self.temp.morse_encode("z"), "--..")

    def test_morse_a_decode(self):
        self.assertEqual(self.temp.morse_decode(".-"), "a")

    def test_morse_d_decode(self):
        self.assertEqual(self.temp.morse_decode("-.."), "d")

    def test_morse_n_decode(self):
        self.assertEqual(self.temp.morse_decode("-."), "n")

    def test_morse_z_decode(self):
        self.assertEqual(self.temp.morse_decode("--.."), "z")

    def test_morse_abc_encode(self):
        self.assertEqual(self.temp.morse_encode("abc"), ".- -... -.-.")

    def test_morse_xyz_encode(self):
        self.assertEqual(self.temp.morse_encode("xyz"), "-..- -.-- --..")

    def test_morse_123_encode(self):
        self.assertEqual(self.temp.morse_encode("123"), ".---- ..--- ...--")

    def test_morse_abc_def_encode(self):
        self.assertEqual(self.temp.morse_encode("abc def"), ".- -... -.-.      -.. . ..-.")

    def test_morse_xyz_123_encode(self):
        self.assertEqual(self.temp.morse_encode("xyz 123"), "-..- -.-- --..      .---- ..--- ...--")

    def test_morse_veni_vidi_encode(self):
        self.assertEqual(self.temp.morse_encode("veni vidi"), "...- . -. ..      ...- .. -.. ..")

    def test_morse_pangram_encode(self):
        self.assertEqual(self.temp.morse_encode("the quick brown fox jumps over the lazy dog"),
                         "- .... .      --.- ..- .. -.-. -.-"
                         "      -... .-. --- .-- -.      ..-. --- -..-"
                         "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
                         "      .-.. .- --.. -.--      -.. --- --.")

    def test_morse_special_chars_encode(self):
        special_chars = ",.?;:/-'" + '"' + "_()=+@"
        special_chars_morse = "--..-- .-.-.- ..--.. -.-.-. ---... -..-. -....- .----. .-..-. ..--.- "
        "-.--. -.--.- -...- .-.-. .--.-."
        self.assertEqual(self.temp.morse_encode(special_chars), special_chars_morse)

    def test_morse_abc_decode(self):
        self.assertEqual(self.temp.morse_decode(".- -... -.-."), "abc")

    def test_morse_xyz_decode(self):
        self.assertEqual(self.temp.morse_decode("-..- -.-- --.."), "xyz")

    def test_morse_123_decode(self):
        self.assertEqual(self.temp.morse_decode(".---- ..--- ...--"), "123")

    def test_morse_abc_def_decode(self):
        self.assertEqual(self.temp.morse_decode(".- -... -.-.      -.. . ..-."), "abc def")

    def test_morse_xyz_123_decode(self):
        self.assertEqual(self.temp.morse_decode("-..- -.-- --..      .---- ..--- ...--"), "xyz 123")

    def test_morse_veni_vidi_decode(self):
        self.assertEqual(self.temp.morse_decode("...- . -. ..      ...- .. -.. .."), "veni vidi")

    def test_morse_pangram_decode(self):
        self.assertEqual(self.temp.morse_decode(
            "- .... .      --.- ..- .. -.-. -.-"
            "      -... .-. --- .-- -.      ..-. --- -..-"
            "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
            "      .-.. .- --.. -.--      -.. --- --."),
                         "the quick brown fox jumps over the lazy dog")

    def test_morse_encode_raises1(self):
        self.assertRaises(ValueError, self.temp.morse_encode, 1)

    def test_morse_encode_raises2(self):
        self.assertRaises(ValueError, self.temp.morse_encode, None)

    def test_morse_encode_raises3(self):
        self.assertRaises(ValueError, self.temp.morse_encode, "ą")

    def test_morse_decode_raises1(self):
        self.assertRaises(ValueError, self.temp.morse_decode, 1)

    def test_morse_decode_raises2(self):
        self.assertRaises(ValueError, self.temp.morse_decode, None)

    def test_morse_decode_raises3(self):
        self.assertRaises(ValueError, self.temp.morse_decode, "ą")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()