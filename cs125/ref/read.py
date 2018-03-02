def main():

    print()
    infile = open("data.txt","r")
    for line in infile:
        print(line, end='')

    print()
    infile.close()

    outfile = open("out.txt", "w")
    print("HelloWorld", file = outfile)
    outfile.close()
    print()

main()
