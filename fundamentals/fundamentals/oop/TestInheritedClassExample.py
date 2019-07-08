import unittest
from InheritedClassExample import InheritedClassExample
from InheritedClassExample import SimpleClass


class TestStringMethods(unittest.TestCase):

    def test_should_return_string_with_suffix_InheritedClassExample(self):
        tested = InheritedClassExample()
        self.assertEqual("The object of class InheritedClassExample welcomes you, Szymon",
                         tested.return_welcome_statement("Szymon"))

    def test_should_return_string_with_suffix_SimpleClass(self):
        tested = SimpleClass()
        self.assertEqual("The object of class SimpleClass welcomes you, Szymon",
                         tested.return_welcome_statement("Szymon"))


if __name__ == '__main__':
    unittest.main()
