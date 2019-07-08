from datetime import timedelta


# simple_timedelta_provider.py
class SimpleTimedeltaProvider:

    def __init__(self):
        pass  # constructor?

    @staticmethod
    def get_year_delta_string():
        return str(timedelta(days=365))
