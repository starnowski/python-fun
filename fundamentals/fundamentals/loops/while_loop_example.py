#https://www.linkedin.com/learning/learning-python-2/loops?u=2159809
#'while' loop example


def main():
    st = ""
    x = 1
    while x < 15:
        st += str(x)
        x += 1
    st += "\nloop with step with value '2'\n"
    x = 1
    while x < 15:
        st += str(x)
        x += 2
    print (st)


if __name__ == "__main__":
    main()