import unittest

from simple_timedelta_provider import SimpleTimedeltaProvider


class TestStringMethods(unittest.TestCase):

    def test_should_return_correct_string_for_year_delta_time(self):
        self.assertEqual("365 days, 0:00:00",
                         SimpleTimedeltaProvider.get_year_delta_string())


if __name__ == '__main__':
    unittest.main()
