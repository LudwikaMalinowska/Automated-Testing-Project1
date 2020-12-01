import unittest
from CaesarCipher.CaesarCipher import CaesarCipher


class CaesarParameterizedFile(unittest.TestCase):

    def test_from_file_cipher(self):
        fileTest = open("../../data/data_caesar_cipher_test")
        tmpCaesar = CaesarCipher()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(",")
                text, caesar_text = str(data[0]), str(data[1].strip("\n"))
                self.assertEqual(tmpCaesar.caesar_cipher(text), caesar_text)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
