
class simpleClass():

    def print_hello(self):
        print "Hello from class 'simpleClass' : " + str(self)

    @staticmethod
    def print_hello_by_class():
        print "Hello from static method for class 'simpleClass'"

    def print_hello_to_someone(self, person_name):
        print "Hello says " + str(self) + " to " + person_name


def main():
    ob = simpleClass()
    ob.print_hello()
    simpleClass.print_hello_by_class()
    ob.print_hello_to_someone("Szymon")


if __name__ == "__main__":
    main()
