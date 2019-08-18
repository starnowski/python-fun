import unittest
import os
from os import path
import yaml
import itertools
import yamale
from yamale import validators


class TestRequiredReferenceValidator(unittest.TestCase):

    schema_file = path.join(os.path.dirname(__file__), "required_reference_validator/schemas/schema.yaml")

    def test_should_return_validation_error_for_invalid_schema(self):
        # given
        test_file = path.join(os.path.dirname(__file__), "required_reference_validator/invalid_data/passenger_seat/infant_without_passenger.yaml")
        with open(test_file, "r") as f:
            yaml_data = yaml.load(f)
            self.assertTrue("passenger_infant_name" in yaml_data, "Yaml should contains property \"passenger_infant_name\"")
            self.assertFalse("passenger_name" in yaml_data, "Yaml should not contains property \"passenger_name\"")

        required_reference_validator = RequiredReferenceValidator(test_file)
        validators_list = validators.DefaultValidators
        validators_list.append()
        yamale_schema = yamale.make_schema(self.schema_file, validators.DefaultValidators)
        yamale_data = itertools.chain(*map(yamale.make_data, yaml))

        # when
        result = yamale.validate(yamale_schema, yamale_data) is not None
        ### TODO


if __name__ == '__main__':
    unittest.main()