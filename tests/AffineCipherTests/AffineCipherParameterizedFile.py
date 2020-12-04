import unittest
from AffineCipher.AffineCipher import AffineCipher


class CaesarParameterizedFile(unittest.TestCase):

    def test_from_file_cipher(self):
        fileTest = open("../../data/data_affine_cipher_test")
        tmpCaesar = AffineCipher()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(",")
                text, a, b, affine_text = str(data[0]), int(data[1]),\
                                          int(data[2]), str(data[3].strip("\n"))
                self.assertEqual(tmpCaesar.affine_cipher(text, a, b), affine_text)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
