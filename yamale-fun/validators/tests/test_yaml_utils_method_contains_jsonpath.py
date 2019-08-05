import unittest
from yaml import load
from validators.src.yaml_utils import YamlFileHelper
import os
from os import path


class TestYamlFileHelper(unittest.TestCase):

    test_file = path.join(os.path.dirname(__file__), "yaml_utils/data.yaml")
    tested = YamlFileHelper(test_file)

    def test_should_return_true_for_existed_main_root_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertTrue("organization" in yaml_data, "Yaml should contains property \"organization\"")

        # when
        result = self.tested.contains_jsonpath("organization")

        # then
        self.assertTrue(result, "YamlFileHelper object should return true that \"organization\" node exists!")

    def test_should_return_false_for_non_existed_main_root_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertFalse("company" in yaml_data, "Yaml should not contains property \"organization\"")

        # when
        result = self.tested.contains_jsonpath("company")

        # then
        self.assertFalse(result, "YamlFileHelper object should return false for node \"company\"!")

    def test_should_return_true_for_existed_child_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertTrue("owner" in yaml_data, "Yaml should contains property \"owner\"")
            self.assertTrue("name" in yaml_data.get("owner"), "Yaml should contains property \"owner.name\"")

        # when
        result = self.tested.contains_jsonpath("owner.name")

        # then
        self.assertTrue(result, "YamlFileHelper object should return true that \"owner.name\" node exists!")

    def test_should_return_false_for_non_existed_child_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertTrue("owner" in yaml_data, "Yaml should contains property \"owner\"")
            self.assertTrue("age" not in yaml_data.get("owner"), "Yaml should not contains property \"owner.age\"")

        # when
        result = self.tested.contains_jsonpath("owner.age")

        # then
        self.assertFalse(result, "YamlFileHelper object should return false for node \"owner.age\"!")