class MorseCode:

    morse_table = {
        "a": "._",
        "b": "_...",
        "c": "_._.",
    }

    def morse_encode(self, text):
        return self.morse_table[text]