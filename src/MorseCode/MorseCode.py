class MorseCode:

    morse_table = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".---.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",

        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",

        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",

        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        ";": "-.-.-.",
        ":": "---...",
        "/": "-..-.",
        "-": "-....-",
        "'": ".----.",
        '"': ".-..-.",
        "_": "..--.-",
        "(": "-.--.",
        ")": "-.--.-",
        "=": "-...-",
        "+": ".-.-.",
        "@": ".--.-.",
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
