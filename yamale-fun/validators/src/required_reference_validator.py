import yamale
from yamale.validators import DefaultValidators, Validator

class Date(Validator):
    """ Custom Date validator """
    tag = 'date'

    def _is_valid(self, value):
        return isinstance(value, datetime.date)