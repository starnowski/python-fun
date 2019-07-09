import unittest
import random


class TestReadFile(unittest.TestCase):

    def test_should_create_new_file_with_content_and_then_read_it(self):
        # given
        file_number = random.randint(1, 99999)

        # when
        f = open(str(file_number) + "_write_test.txt", "w+")
        self.f = f
        f.write("first line\n")
        f.write("second line")
        f.close()

        # then
        f = open(str(file_number) + "_write_test.txt", "r")
        self.f = f
        fl = f.readlines()
        self.assertEqual("first line\n", fl[0])
        self.assertEqual("second line", fl[1])

    def test_should_return_all_lines_in_file(self):
        f = open("test1.txt", "r")
        self.f = f
        fl = f.readlines()
        self.assertEqual("Ala ma kota\n", fl[0])
        self.assertEqual("Ola ma psa", fl[1])

    def tearDown(self):
        self.f.close()


if __name__ == '__main__':
    unittest.main()
