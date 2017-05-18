def main():
    print()

    string = input("Enter the character that need to be put on the waves~~~")
    blanks = 0

    while blanks <= 40:
        for i in range (0,16):
            print(blanks * " ", string)

            blanks = blanks + i

            if blanks > 40:
                for i in range(0, 16):
                    blanks = blanks - 16 + i
                    print(blanks * " ", string)







main()