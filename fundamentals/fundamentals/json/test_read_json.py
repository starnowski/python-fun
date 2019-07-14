import unittest
import json


class TestReadJson(unittest.TestCase):

    def test_read_json_data(self):
        # given
        with open("test_json/test1.json", "r") as f:

            # when
            json_data = json.load(f)

            # then
            self.assertTrue("name" in json_data, "Json should contains property \"name\"")
            self.assertTrue("firstName" in json_data, "Json should contains property \"firstName\"")
            self.assertTrue("lastName" in json_data, "Json should contains property \"lastName\"")
            self.assertTrue("githubRepositories" in json_data, "Json should contains property \"githubRepositories\"")
