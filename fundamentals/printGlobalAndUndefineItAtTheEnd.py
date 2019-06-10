## File demonstrate how global scope works

var = 1099


def someFun():
    global var
    var = 2000
    print(var)

print(var)
someFun()
del var
print(var)

# Expected output:
#1099
#2000
#Some stack with an error --> Why this is printed at the begining of console?