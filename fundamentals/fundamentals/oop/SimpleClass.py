
class SimpleClass:

    def __init__(self):
        pass  # constructor?

    def print_hello(self):
        print "Hello from class 'SimpleClass' : " + str(self)

    @staticmethod
    def print_hello_by_class():
        print "Hello from static method for class 'SimpleClass'"

    def print_hello_to_someone(self, person_name):
        print "Hello says " + str(self) + " to " + person_name


def main():
    ob = SimpleClass()  # initializing object of type simpleClass
    ob.print_hello()
    SimpleClass.print_hello_by_class()
    ob.print_hello_to_someone("Szymon")


if __name__ == "__main__":
    main()
