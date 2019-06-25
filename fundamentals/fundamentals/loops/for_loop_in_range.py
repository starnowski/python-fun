#https://www.linkedin.com/learning/learning-python-2/loops?u=2159809
#Range loop example


def main():
    st = ""
    for x in range(5, 15):
        st += str(x)
    st += "\nloop with step with value '2'\n"
    for x in range(5, 15, 2):
        st += str(x)
    print (st)


if __name__ == "__main__":
    main()