#https://www.linkedin.com/learning/learning-python-2/conditional-structures?u=2159809


def main():
    x, y = 100, 100
    print("In main function")
    if (x == y):
        st = "x equals y"
    else:
        st = "x does note equals y"

    a , b = 10, 100
    if (a < b):
        abst = "a is less than b"
    else:
        abst = "a is not less than b"

    print(st)
    print(abst)
    print(return_statement_about_comparing_integers(7, 10))
    print(return_statement_about_comparing_integers(7, 7))
    print(return_statement_about_comparing_integers(10, 7))


def return_statement_about_comparing_integers(left, right):
    if left == right:
        return "left equals right"
    elif left > right:
        return "left is bigger right"
    else:
        return "left is lower right"

if __name__ == "__main__":
    main()