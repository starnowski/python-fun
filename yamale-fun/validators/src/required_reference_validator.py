import yamale
from yamale.validators import DefaultValidators, Validator

class RequiredReferenceValidator(Validator):
    """ Custom Date validator """
    tag = 'ref_req'

    def __init__(self, *args, **kwargs):
        self.validators = [val for val in args if isinstance(val, Validator)]
        super(RequiredReferenceValidator, self).__init__(*args, **kwargs)

    def _is_valid(self, value):
        return True
