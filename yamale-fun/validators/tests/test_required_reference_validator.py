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

    def test_should_return_true_for_valid_document_with_all_properties(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "required_reference_validator/valid_data/passenger_seat/passenger_with_infant.yaml")
        with open(test_file, "r") as f:
            yaml_data = yaml.load(f)
            self.assertTrue("passenger_infant_name" in yaml_data, "Yaml should contains property \"passenger_infant_name\"")
            self.assertTrue("passenger_name" in yaml_data, "Yaml should contains property \"passenger_name\"")

        # when
        result = tested.validate(test_file)

        # then
        self.assertTrue(result, "Validator should return true")

    def test_should_return_true_for_valid_document_without_optional_property(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "required_reference_validator/valid_data/passenger_seat/passenger_without_infant.yaml")
        with open(test_file, "r") as f:
            yaml_data = yaml.load(f)
            self.assertFalse("passenger_infant_name" in yaml_data, "Yaml should not contains property \"passenger_infant_name\" which is optional property")
            self.assertTrue("passenger_name" in yaml_data, "Yaml should contains property \"passenger_name\"")

        # when
        result = tested.validate(test_file)

        # then
        self.assertTrue(result, "Validator should return true")


if __name__ == '__main__':
    unittest.main()