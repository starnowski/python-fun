## File demonstrate how global scope works

var = 1099


def someFun():
    global var
    var = 2000
    print(var)

print(var)
someFun()
print(var)

# Expected output:
#1099
#2000
#2000