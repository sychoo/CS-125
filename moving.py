# File: moving.py
# Author: Simon Chu
# Date: 2/22/17
# Purpose: encode and decode a sentence
#          moving characters 13 places.

def main():
    print()
    print("Program to encode and decode a sentence")
    print("moving characters 13 places.")
    print("You will be asked to enter a sentence.")
    print("Written by Simon Chu.")
    print()

    sentence = input("Enter a sentence: ")
    print()
    print() # for turnin

    # encode the sentence
    cipherText = ""
    for ch in sentence:
        outChar = ch

        # for lowercase letters
        if ch >= "a":
            if ch <= "z":
                outChar = chr(ord(ch) + 13)

                if outChar > "z":
                    outChar = chr(ord(ch) - 13)

                if outChar < "a":
                    outChar = chr(ord(ch) + 13)

        # for uppercase letters
        if ch >= "A":
            if ch <= "Z":
                outChar = chr(ord(ch) + 13)

                if outChar > "Z":
                    outChar = chr(ord(ch) - 13)

                if outChar < "A":
                    outChar = chr(ord(ch) + 13)

        cipherText = cipherText + outChar

    # decode the sentence
    decodeText = ""
    for ch in cipherText:
        outChar = ch

        # for lowercase letters
        if ch >= "a":
            if ch <= "z":
                outChar = chr(ord(ch) + 13)

                if outChar > "z":
                    outChar = chr(ord(ch) - 13)

                if outChar < "a":
                    outChar = chr(ord(ch) + 13)

        # for uppercase letters
        if ch >= "A":
            if ch <= "Z":
                outChar = chr(ord(ch) + 13)

                if outChar > "Z":
                    outChar = chr(ord(ch) - 13)

                if outChar < "A":
                    outChar = chr(ord(ch) + 13)

        decodeText = decodeText + outChar

    # print results
    print("Original sentence:", sentence)
    print("Encoded version:  ", cipherText)
    print("Decoded version:  ", decodeText)

    print()


main()