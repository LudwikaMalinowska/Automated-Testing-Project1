
class CaesarCipher:
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

    def caesar_cipher(self, text):

        if not isinstance(text, str):
            raise ValueError

        ciphered = ""
        for letter in text:
            if letter == " ":
                ciphered += " "
                continue

            if letter not in self.letters:
                raise ValueError(f"Key {letter} not found")

            letterNr = self.letters[letter]
            letterNr += 3

            letterNr %= 26
            ciphered += self.reverse_letters[letterNr]

        return ciphered

    def caesar_decipher(self, caesar_text):

        if not isinstance(caesar_text, str):
            raise ValueError

        deciphered = ""
        for letter in caesar_text:
            if letter == " ":
                deciphered += " "
                continue

            letterNr = self.letters[letter]
            letterNr -= 3

            letterNr %= 26
            deciphered += self.reverse_letters[letterNr]

        return deciphered

