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
            self.assertEqual(4, json_data["githubRepositories"].__len__(), "The array \"githubRepositories\" should contains four objects")
            self.assertEqual("docker-fun", json_data["githubRepositories"][0]["name"], "First mentioned repository should be \"docker-fun\"")
            self.assertEqual("posmulten", json_data["githubRepositories"][1]["name"], "Second mentioned repository should be \"posmulten\"")
            self.assertEqual("bmunit-extension", json_data["githubRepositories"][2]["name"], "Third mentioned repository should be \"bmunit-extension\"")
            self.assertEqual("bash-fun", json_data["githubRepositories"][3]["name"], "Fourth mentioned repository should be \"bash-fun\"")
