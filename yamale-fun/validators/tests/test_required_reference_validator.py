import unittest
import os
from os import path
import yaml
import itertools
import yamale
from yamale import validators

from validators.src.required_reference_validator import RequiredReferenceValidator, YamaleRequiredReferenceFacade


class TestRequiredReferenceValidator(unittest.TestCase):

    schema_file = path.join(os.path.dirname(__file__), "required_reference_validator/schemas/schema.yml")

    def test_should_return_validation_error_for_invalid_schema(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "required_reference_validator/invalid_data/passenger_seat/infant_without_passenger.yaml")
        with open(test_file, "r") as f:
            yaml_data = yaml.load(f)
            self.assertTrue("passenger_infant_name" in yaml_data, "Yaml should contains property \"passenger_infant_name\"")
            self.assertFalse("passenger_name" in yaml_data, "Yaml should not contains property \"passenger_name\"")

        try:
            # when
            tested.validate(test_file)
            self.fail("Expected ValueError")

        except ValueError:
            # then
            pass


if __name__ == '__main__':
    unittest.main()