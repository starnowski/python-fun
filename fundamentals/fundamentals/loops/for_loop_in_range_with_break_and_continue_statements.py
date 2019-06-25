#https://www.linkedin.com/learning/learning-python-2/loops?u=2159809
#Range loop example


def main():
    st = "even numbers between 1 and 10\n"
    for x in range(1, 11):
        if (x % 2 == 1):
            continue
        st += str(x)
    st += "\nodd numbers between 1 and 10\n"
    for x in range(1, 11):
        if (x % 2 == 0):
            continue
        st += str(x)
    st += "\nnumbers less then 5\n"
    for x in range(1, 11):
        if (x == 5):
            break
        st += str(x)
    print (st)


if __name__ == "__main__":
    main()