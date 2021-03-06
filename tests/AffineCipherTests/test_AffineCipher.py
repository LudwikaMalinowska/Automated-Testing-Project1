import unittest

from AffineCipher.AffineCipher import AffineCipher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_a_cipher(self):
        self.assertEqual(self.temp.affine_cipher("a", 1, 3), "d")

    def test_z_cipher(self):
        self.assertEqual(self.temp.affine_cipher("z", 1, 3), "c")

    def test_abc_cipher(self):
        self.assertEqual(self.temp.affine_cipher("abc", 3, 12), "mps")

    def test_veni_vidi_cipher(self):
        self.assertEqual(self.temp.affine_cipher("veni vidi", 3, 12), "xyzk xkvk")

    def test_pangram_cipher(self):
        self.assertEqual(self.temp.affine_cipher("the quick brown fox jumps over the lazy dog", 3, 12),
                         "rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce")

    def test_a_decipher(self):
        self.assertEqual(self.temp.affine_decipher("d", 1, 3), "a")

    def test_z_decipher(self):
        self.assertEqual(self.temp.affine_decipher("c", 1, 3), "z")

    def test_abc_decipher(self):
        self.assertEqual(self.temp.affine_decipher("mps", 3, 12), "abc")

    def test_veni_decipher(self):
        self.assertEqual(self.temp.affine_decipher("xyzk", 3, 12), "veni")

    def test_veni_vidi_decipher(self):
        self.assertEqual(self.temp.affine_decipher("xyzk xkvk", 3, 12), "veni vidi")

    def test_pangram_decipher(self):
        self.assertEqual(self.temp.affine_decipher("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce", 3, 12),
                         "the quick brown fox jumps over the lazy dog")

    def test_cipher_exception1(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, 1, 1, 3)

    def test_cipher_exception2(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, None, 1, 3)

    def test_cipher_exception3(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, "ą", 1, 3)

    def test_cipher_exception4(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, "abc", -1, 3)

    def test_cipher_exception5(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, "abc", 3, -12)

    def test_cipher_exception6(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, "abc", "3", 12)

    def test_cipher_exception7(self):
        self.assertRaises(ValueError, self.temp.affine_cipher, "abc", 3, "12")

    def test_decipher_exception1(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, 1, 1, 3)

    def test_decipher_exception2(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, None, 1, 3)

    def test_decipher_exception3(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, "ą", 1, 3)

    def test_decipher_exception4(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, "abc", -1, 3)

    def test_decipher_exception5(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, "abc", 3, -12)

    def test_decipher_exception6(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, "abc", "3", 12)

    def test_decipher_exception7(self):
        self.assertRaises(ValueError, self.temp.affine_decipher, "abc", 3, "12")



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
