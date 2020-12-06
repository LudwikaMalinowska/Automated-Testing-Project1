from MorseCode.MorseCode import MorseCode
from CaesarCipher.CaesarCipher import CaesarCipher
from AffineCipher.AffineCipher import AffineCipher


print("Wybierz sposób szyfrowania: ")
print("1. Alfabet Morsa")
print("2. Szyfr Cezara")
print("3. Szyfr Afiniczny")
cipher_type = input()

if cipher_type == "1":
    print("1. Tekst na Alfabet Morsa")
    print("2. Alfabet Morsa na tekst")
    morse = MorseCode()
    nr = input()
    if nr == "1":
        text = input("Podaj text: ")
        morse_text = morse.morse_encode(text)
        print(morse_text)
    elif nr == "2":
        morse_text = input("Podaj text: ")
        text = morse.morse_encode(morse_text)
        print(text)
    else:
        print("Podaj prawidłowy numer")

elif cipher_type == "2":
    ...
elif cipher_type == "3":
    ...

else:
    print("Podaj prawidłowy numer")