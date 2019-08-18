import yamale
from yamale.validators import DefaultValidators, Validator

class RequiredReferenceValidator(Validator):
    """ Custom Date validator """
    tag = 'ref_req'

    def _is_valid(self, value):
        return isinstance(value, datetime.date)