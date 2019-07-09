import unittest


class TestReadFile(unittest.TestCase):

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
