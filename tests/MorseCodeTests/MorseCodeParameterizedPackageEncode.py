import unittest
from MorseCode.MorseCode import MorseCode
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class MorseCodeParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    @parameterized.expand([
        ("a", ".-"),
        ("d", "-.."),
        ("n", "-."),
        ("z", "--.."),
        ("abc", ".- -... -.-."),
        ("xyz", "-..- -.-- --.."),
        ("123", ".---- ..--- ...--"),
        ("abc def", ".- -... -.-.      -.. . ..-."),
        ("xyz 123", "-..- -.-- --..      .---- ..--- ...--"),
        ("veni vidi", "...- . -. ..      ...- .. -.. .."),
        ("the quick brown fox jumps over the lazy dog",
         "- .... .      --.- ..- .. -.-. -.-"
         "      -... .-. --- .-- -.      ..-. --- -..-"
         "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
         "      .-.. .- --.. -.--      -.. --- --."
         )

    ])
    def test_one_parameterized(self, text, result):
        self.assertEqual(self.tmp.morse_encode(text), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("a", ".-"),
    ("d", "-.."),
    ("n", "-."),
    ("z", "--.."),
    ("abc", ".- -... -.-."),
    ("xyz", "-..- -.-- --.."),
    ("123", ".---- ..--- ...--"),
    ("abc def", ".- -... -.-.      -.. . ..-."),
    ("xyz 123", "-..- -.-- --..      .---- ..--- ...--"),
    ("veni vidi", "...- . -. ..      ...- .. -.. .."),
    ("the quick brown fox jumps over the lazy dog",
     "- .... .      --.- ..- .. -.-. -.-"
     "      -... .-. --- .-- -.      ..-. --- -..-"
     "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
     "      .-.. .- --.. -.--      -.. --- --."
     )

])
def test_morse_encode_outside_class(text, result):
    r = MorseCode()
    assert_equal(r.morse_encode(text), result)


@parameterized_class(('text', 'result'), [
    ("a", ".-"),
    ("d", "-.."),
    ("n", "-."),
    ("z", "--.."),
    ("abc", ".- -... -.-."),
    ("xyz", "-..- -.-- --.."),
    ("123", ".---- ..--- ...--"),
    ("abc def", ".- -... -.-.      -.. . ..-."),
    ("xyz 123", "-..- -.-- --..      .---- ..--- ...--"),
    ("veni vidi", "...- . -. ..      ...- .. -.. .."),
    ("the quick brown fox jumps over the lazy dog",
     "- .... .      --.- ..- .. -.-. -.-"
     "      -... .-. --- .-- -.      ..-. --- -..-"
     "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
     "      .-.. .- --.. -.--      -.. --- --."
     )

])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.morse_encode(self.text), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
