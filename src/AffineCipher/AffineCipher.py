
class AffineCipher:
    letters = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,

        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25
    }

    reverse_letters = {v: k for k, v in letters.items()}

    def affine_cipher(self, text, a, b):
        ciphered = ""
        for letter in text:
            if letter == " ":
                ciphered += " "
                continue

            letterNr = self.letters[letter]
            letterNr *= a
            letterNr += b
            letterNr %= 26

            ciphered += self.reverse_letters[letterNr]
        return ciphered

    def affine_decipher(self, affine_text, a, b):
        letterNr = self.letters[affine_text]
        letterNr = letterNr - b
        letterNr /= a
        return self.reverse_letters[letterNr]

