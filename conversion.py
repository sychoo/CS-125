var = input("var: ")
try:
    var != int(var)
except ValueError:
    print ("var is a str")
