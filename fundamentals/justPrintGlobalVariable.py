## File demonstrate how global scope works

var = 1099


def someFun():
    print("Global variable is : " + str(var))

print(var)
someFun()
