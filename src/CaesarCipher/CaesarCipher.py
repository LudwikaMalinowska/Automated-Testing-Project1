
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
        # return self.reverse_letters[self.letters[text] + 3]

        ciphered = ""
        for letter in text:
            if letter == " ":
                ciphered += " "
                continue

            letterNr = self.letters[letter]
            letterNr += 3
            # if letterNr > 25:
            #     letterNr -= 26

            letterNr %= 26
            ciphered += self.reverse_letters[letterNr]

        return ciphered


    def caesar_decipher(self, caesar_text):

        deciphered = ""
        for letter in caesar_text:
            nr = self.letters[letter]
            nr = nr - 3

            if nr < 0:
                nr += 26

            deciphered += self.reverse_letters[nr]

        return deciphered

