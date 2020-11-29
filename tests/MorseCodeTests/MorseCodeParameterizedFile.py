import unittest
from MorseCode.MorseCode import MorseCode


class FizzBuzzParameterizedFile(unittest.TestCase):

    def test_from_file_encode(self):
        fileTest = open("../../data/data_morse_encode_test")
        tmpMorse = MorseCode()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(",")
                text, morse = str(data[0]), str(data[1].strip("\n"))
                self.assertEqual(tmpMorse.morse_encode(text), morse)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()