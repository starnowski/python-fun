import unittest
import os
from zipfile import ZipFile
from os import path
import shutil


class TestListDirectory(unittest.TestCase):

    def test_should_correctly_archive_test_directory(self):
        # given
        test_dir_name = "test1_dir"
        test_dir_archive_name = "test1_dir_archive.zip"
        test_extracted_dir = "extracted_dir"
        self.assertFalse(path.exists(test_dir_archive_name), "Test archive should not exist yet!")
        self.assertFalse(path.exists(test_extracted_dir), "Test extracted dir should not exist yet!")

        try:
            # when
            with ZipFile(test_dir_archive_name, "w") as zip_file:
                zip_file.write(test_dir_name)

            with ZipFile(test_dir_archive_name, "r") as zip_file:
                zip_file.extractall(test_extracted_dir)

            files = os.listdir(test_extracted_dir)

            # then
            self.assertTrue(files.__contains__("test1"), "Directory should contains file \"test1\"")
            self.assertTrue(files.__contains__("test2"), "Directory should contains file \"test2\"")
            self.assertEqual(2, files.__len__(), "Directory should contains two files only")

        finally:
            if path.exists(test_dir_archive_name):
                os.remove(test_dir_archive_name)
            if path.exists(test_extracted_dir):
                shutil.rmtree(test_extracted_dir)


if __name__ == '__main__':
    unittest.main()
