
n = input("Hello")
try:
    n = float(n)
except ValueError:
    print("Error: option # must be a valid number, not \""
          + str(n) + "\".")
print(n)


