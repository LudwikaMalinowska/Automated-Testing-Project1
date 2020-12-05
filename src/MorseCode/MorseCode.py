class MorseCode:

    morse_table = {
        "a": "._",
        "b": "_...",
        "c": "_._.",
        "d": "_..",
        "e": ".",
        "f": ".._.",
        "g": "__.",
        "h": "....",
        "i": "..",
        "j": ".___",
        "k": "_._",
        "l": "._..",
        "m": "__",
        "n": "_.",
        "o": "___",
        "p": ".__.",
        "q": "__._",
        "r": "._.",
        "s": "...",
        "t": "_",

        "u": ".._",
        "v": "..._",
        "w": ".__",
        "x": "_.._",
        "y": "_.__",
        "z": "__..",

        "1": ".____",
        "2": "..___",
        "3": "...__",
        "4": "...._",
        "5": ".....",
        "6": "_....",
        "7": "__...",
        "8": "___..",
        "9": "____.",
        "0": "_____",
    }

    reverse_morse_table = {v: k for k, v in morse_table.items()}

    def morse_encode(self, text):
        if not isinstance(text, str):
            raise ValueError

        morse_text = ""

        for i in range(len(text)):
            if text[i] == " ":
                morse_text += "     "
            else:
                letter = text[i]
                if letter not in self.morse_table:
                    raise ValueError(f"Key {letter} not found")

                morseLetter = self.morse_table[letter]
                if i == len(text) - 1:
                    morse_text += morseLetter
                else:
                    morse_text += morseLetter + " "

        return morse_text

    def morse_decode(self, morseText):

        if not isinstance(morseText, str):
            raise ValueError

        text = ""
        morse_tab = morseText.split(" ")

        space = 0
        for m in morse_tab:
            if m == "":
                space += 1
                if space == 5:
                    text += " "
                    space = 0
                continue
            else:
                if m not in self.reverse_morse_table:
                    raise ValueError(f"Key {m} not found")
                letter = self.reverse_morse_table[m]
                text += letter

        return text
