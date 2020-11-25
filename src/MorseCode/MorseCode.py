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
    }

    def morse_encode(self, text):
        return self.morse_table[text]