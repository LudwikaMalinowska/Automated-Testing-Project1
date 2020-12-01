
class CaesarCipher:
    letters = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
    }

    reverse_letters = {v: k for k, v in letters.items()}

    def caesar_cipher(self, text):
        return self.reverse_letters[self.letters[text] + 3]

    def caesar_decipher(self, caesar_text):
        ...

