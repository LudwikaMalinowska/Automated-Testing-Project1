
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

        if not isinstance(text, str):
            raise ValueError

        if a <= 0:
            raise ValueError("Parametr a musi być dodatni")

        ciphered = ""
        for letter in text:
            if letter == " ":
                ciphered += " "
                continue

            if letter not in self.letters:
                raise ValueError(f"Key {letter} not found")

            letterNr = self.letters[letter]
            letterNr *= a
            letterNr += b
            letterNr %= 26

            ciphered += self.reverse_letters[letterNr]
        return ciphered

    def affine_decipher(self, affine_text, a, b):

        if not isinstance(affine_text, str):
            raise ValueError

        deciphered = ""
        for letter in affine_text:
            if letter == " ":
                deciphered += " "
                continue

            if letter not in self.letters:
                raise ValueError(f"Key {letter} not found")

            letterNr = self.letters[letter]
            letterNr = letterNr - b

            letterNr %= 26
            while not letterNr % a == 0:
                letterNr += 26

            letterNr /= a
            deciphered += self.reverse_letters[letterNr]
        return deciphered

