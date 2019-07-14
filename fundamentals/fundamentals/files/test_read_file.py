import unittest
import random
import os
from os import path


class TestReadFile(unittest.TestCase):

    def test_should_create_new_file_with_content_and_then_read_it(self):
        # given
        random_number = random.randint(1, 99999)
        self.created_test_file = str(random_number) + "_write_test.txt"

        # when
        f = open(self.created_test_file, "w+")
        self.f = f
        f.write("first line\n")
        f.write("second line")
        f.close()

        # then
        f = open(self.created_test_file, "r")
        self.f = f
        fl = f.readlines()
        self.assertEqual("first line\n", fl[0])
        self.assertEqual("second line", fl[1])

    def test_should_create_new_file_with_content_and_then_append_it(self):
        # given
        random_number = random.randint(1, 99999)
        self.created_test_file = str(random_number) + "_write_test.txt"

        # when
        f = open(self.created_test_file, "w+")
        self.f = f
        f.write("first line\n")
        f.write("second line")
        f.close()

        f = open(self.created_test_file, "a")
        self.f = f
        f.write("\nthird line\n")
        f.write("fourth line")
        f.close()

        # then
        f = open(self.created_test_file, "r")
        self.f = f
        fl = f.readlines()
        self.assertEqual("first line\n", fl[0])
        self.assertEqual("second line\n", fl[1])
        self.assertEqual("third line\n", fl[2])
        self.assertEqual("fourth line", fl[3])

    def test_should_return_all_lines_in_file(self):
        # given
        f = open("test1.txt", "r")
        self.f = f

        # when
        fl = f.readlines()

        # then
        self.assertEqual("Ala ma kota\n", fl[0])
        self.assertEqual("Ola ma psa", fl[1])

    def test_should_return_all_lines_in_file_in_the_with_section(self):
        # given
        with open("test1.txt", "r") as f: # 'with' statement - https://docs.python.org/2.5/whatsnew/pep-343.html
            # when
            fl = f.readlines()

            # then
            self.assertEqual("Ala ma kota\n", fl[0])
            self.assertEqual("Ola ma psa", fl[1])

    def tearDown(self):
        if hasattr(self, 'f'):
            self.f.close()

        if hasattr(self, 'created_test_file') and path.exists(self.created_test_file):
                os.remove(self.created_test_file)


if __name__ == '__main__':
    unittest.main()
