#https://www.linkedin.com/learning/learning-python-2/loops?u=2159809
#'for' loop example for collection items


def main():
    st = "Days of the week "
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        st += day + " "
    print (st)


if __name__ == "__main__":
    main()
