from MorseCode.MorseCode import MorseCode
from CaesarCipher.CaesarCipher import CaesarCipher
from AffineCipher.AffineCipher import AffineCipher
import requests
from bs4 import BeautifulSoup

class CipherAll:

    def print_morse(self):
        print("1. Tekst na Alfabet Morsa")
        print("2. Alfabet Morsa na tekst")
        morse = MorseCode()
        nr = input()
        if nr == "1":
            print("1. Wpisz tekst ręcznie")
            print("2. Tekst z linku")
            text_nr = input("Podaj nr: ")

            if text_nr == "1":
                text = input("Podaj text: ")
                morse_text = morse.morse_encode(text)
                print(morse_text)

            elif text_nr == "2":
                link = input("Podaj link: ")
                response = requests.get(link)

                if response.status_code == 200:
                    html_doc = response.content
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    text = soup.get_text()
                    text = text.lower()
                    text2 = ""
                    for letter in text:
                        if letter == " ":
                            text2 += " "
                            continue
                        if letter in morse.morse_table:
                            text2 += letter
                    print("Tekst z linku: ", text2)
                    print("Tekst w alfabecie morsa: ")
                    morse_text = morse.morse_encode(text2)
                    print(morse_text)

            else:
                print("Podaj prawidłowy numer")


        elif nr == "2":
            morse_text = input("Podaj text: ")
            text = morse.morse_decode(morse_text)
            print(text)


    def print_caesar(self):
        print("1. Tekst na Szyfr Cezara")
        print("2. Szyfr Cezara na tekst")
        caesar = CaesarCipher()
        nr = input()
        if nr == "1":
            print("1. Wpisz tekst ręcznie")
            print("2. Tekst z linku")
            text_nr = input("Podaj nr: ")

            if text_nr == "1":
                text = input("Podaj text: ")
                ces_text = caesar.caesar_cipher(text)
                print(ces_text)

            elif text_nr == "2":
                link = input("Podaj link: ")
                response = requests.get(link)

                if response.status_code == 200:
                    html_doc = response.content
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    text = soup.get_text()
                    text = text.lower()
                    text2 = ""
                    for letter in text:
                        if letter == " ":
                            text2 += " "
                            continue
                        if letter in caesar.letters:
                            text2 += letter
                    print("Tekst z linku: ", text2)
                    print("Tekst zaszyfrowany: ")
                    ces_text = caesar.caesar_cipher(text2)
                    print(ces_text)


        elif nr == "2":
            caesar_text = input("Podaj text: ")
            text = caesar.caesar_decipher(caesar_text)
            print(text)
        else:
            print("Podaj prawidłowy numer")

    def print_affine(self):
        print("1. Tekst na Szyfr Afiniczny")
        print("2. Szyfr Afiniczny na tekst")
        aff = AffineCipher()
        nr = input()
        if nr == "1":
            a = int(input("Podaj parametr a: "))
            b = int(input("Podaj parametr b: "))

            print("1. Wpisz tekst ręcznie")
            print("2. Tekst z linku")
            text_nr = input("Podaj nr: ")

            if text_nr == "1":
                text = input("Podaj text: ")
                aff_text = aff.affine_cipher(text, a, b)
                print(aff_text)

            elif text_nr == "2":
                link = input("Podaj link: ")
                response = requests.get(link)

                if response.status_code == 200:
                    html_doc = response.content
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    text = soup.get_text()
                    text = text.lower()
                    text2 = ""
                    for letter in text:
                        if letter == " ":
                            text2 += " "
                            continue
                        if letter in aff.letters:
                            text2 += letter
                    print("Tekst z linku: ", text2)
                    print("Tekst zaszyfrowany: ")
                    aff_text = aff.affine_cipher(text2, a, b)
                    print(aff_text)


        elif nr == "2":
            aff_text = input("Podaj text: ")
            a = int(input("Podaj parametr a: "))
            b = int(input("Podaj parametr b: "))
            text = aff.affine_decipher(aff_text, a, b)
            print(text)
        else:
            print("Podaj prawidłowy numer")

    def main(self):
        while True:
            print("Wybierz sposób szyfrowania: ")
            print("1. Alfabet Morsa")
            print("2. Szyfr Cezara")
            print("3. Szyfr Afiniczny")
            print("4. Zamknij program")
            cipher_type = input()

            if cipher_type == "1":
                self.print_morse()
            elif cipher_type == "2":
                self.print_caesar()
            elif cipher_type == "3":
                self.print_affine()
            elif cipher_type == "4":
                break
            else:
                print("Podaj prawidłowy numer")
