from yamale import YamaleTestCase
import os


class TestAnyValidatorSchemaValidData(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = 'schemas/any_validator/schema_any_validator.yaml'
    data_dir_name = 'data/any_validator/valid_data'
    yaml = [data_dir_name + '/*.yaml']

    def runTest(self):
        # given
        data_dir_name = os.path.join(self.base_dir, self.data_dir_name)
        files = os.listdir(data_dir_name)
        #
        # https://www.geeksforgeeks.org/python-output-formatting/ - useful description how to format string
        #
        self.assertGreater(files.__len__(), 0, "Directory '%s' with test data files should contains at least one file" %data_dir_name)

        # when
        is_valid = self.validate()

        # then
        self.assertTrue(is_valid)
