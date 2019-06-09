## File demonstrate how global and local scopes works

var = 1099


def someFun():
    var = "ABC"
    print(var)

print(var)
someFun()
print(var)

# Expected output:
#1099
#ABC
#1099