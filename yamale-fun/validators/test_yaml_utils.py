import unittest
from yaml import load

from validators.yaml_utils import YamlFileHelper


class YamlFileHelperTest(unittest.TestCase):

    test_file = "test/yaml_utils/data.yaml"
    tested = YamlFileHelper(test_file)

    def test_should_return_true_for_existed_main_root_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertTrue("organization" in yaml_data, "Json should contains property \"name\"")

        # when
        result = self.tested.contains_jsonpath("organization")

        # then
        self.assertTrue(result, "YamlFileHelper object should return true that \"organization\" node exists!")