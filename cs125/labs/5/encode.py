# File: encode.py
# Author: Simon Chu
# Date: 2/16/17
# Purpose: Encode and decode the message.

def main():

    print()
    print("This program will encode a message using")
    print("a Caesar cipher.")
    print("You will enter a key (number between -25 and 25). ")
    print("Written by Simon Chu")
    print()

    key = int(input("Enter a key (number between -25 and 25): "))

    if key < -25:
        print("Error, key must be >= -25 , not", key)
        exit()

    if key > 25:
        print("Error, key must be <=25, not", key)
        exit()
        
    print() # for turnin
    print()
    plaintext = input("Enter a sentence: ")
    print() # for turnin
    print()
    small = plaintext.lower()
    print("With a key of", key)
    print()
    
    print("Original line:", small)
    print()

    ciphertext = ""
    for ch in small:
        outChar = ch

        if ch >= "a":
            if ch <= "z":
                

                outChar = chr(ord(ch) + key)

                if outChar > "z":
                    outChar = chr(ord(ch) + key - 26)

                if outChar < "a":
                    outChar = chr(ord(ch) + key + 26)

        ciphertext = ciphertext + outChar

    print("Encoded line: ", ciphertext)
    print()
    

              
main()
