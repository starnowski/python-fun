import unittest
import random
import os
from os import path


class TestListDirectory(unittest.TestCase):

    def test_should_correctly_list_directory(self):
        # given
        test_dir_name = "test1_dir"

        # when
        files = os.listdir(test_dir_name)

        # then
        self.assertTrue(files.__contains__("test1"), "Directory should contains file \"test1\"")
        self.assertTrue(files.__contains__("test2"), "Directory should contains file \"test2\"")


if __name__ == '__main__':
    unittest.main()
