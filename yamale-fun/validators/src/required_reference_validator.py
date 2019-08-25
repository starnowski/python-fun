import yamale
from yamale.validators import DefaultValidators, Validator
import yaml
import itertools
import yamale
from yamale import validators

class YamaleRequiredReferenceFacade():

    def __init__(self, schema_file):
        validators_list = validators.DefaultValidators
        validators_list[RequiredReferenceValidator.__name__] = RequiredReferenceValidator
        validators_list[RequiredReferenceValidator.tag] = RequiredReferenceValidator
        self.yamale_schema = yamale.make_schema(schema_file, validators=validators_list)

    def validate(self, data_file_path):
        yamale_data = itertools.chain(*map(yamale.make_data, [data_file_path]))
        return yamale.validate(self.yamale_schema, yamale_data) is not None


class RequiredReferenceValidator(Validator):
    tag = 'ref_req'

    def __init__(self, *args, **kwargs):
        self.validators = [val for val in args if isinstance(val, Validator)]
        self.is_required = False
        super(RequiredReferenceValidator, self).__init__(*args, **kwargs)

    def _is_valid(self, value):
        return True

    @property
    def is_optional(self):
        return not self.is_required
