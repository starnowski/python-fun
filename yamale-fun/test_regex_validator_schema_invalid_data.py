from yamale import YamaleTestCase
import os


class TestRegexValidatorSchemaInvalidData(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = 'schemas/regex_validator/schema_regex_validator.yaml'
    data_dir_name = 'data/regex_validator/invalid_data'
    yaml = [data_dir_name + '/*.yaml']

    def runTest(self):
        # given
        data_dir_name = os.path.join(self.base_dir, self.data_dir_name)
        files = os.listdir(data_dir_name)
        self.assertGreater(files.__len__(), 0, "Directory '%s' with test data files should contains at least one file" %data_dir_name)

        try:
            # when
            self.validate()
            self.fail("Expected ValueError")
        except ValueError:
            # then
            pass
