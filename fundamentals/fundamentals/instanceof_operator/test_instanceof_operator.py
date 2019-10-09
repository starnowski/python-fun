import unittest


class InstanceOfOperatorTestCase(unittest.TestCase):

    def setUp(self):
        self.test_tuple = (1, 3)
        self.test_list = [8, 43, 1]

    def test_instanceof_operator_should_return_true_for_correct_type_match(self):
        # when
        test_tuple_is_tuple_type = isinstance(self.test_tuple, tuple)
        test_list_is_list_type = isinstance(self.test_list, list)

        # then
        self.assertTrue(test_tuple_is_tuple_type)
        self.assertTrue(test_list_is_list_type)

    def test_instanceof_operator_should_return_false_for_incorrect_type_match(self):
        # when
        test_tuple_is_list_type = isinstance(self.test_tuple, list)
        test_list_is_tuple_type = isinstance(self.test_list, tuple)

        # then
        self.assertFalse(test_tuple_is_list_type)
        self.assertFalse(test_list_is_tuple_type)

if __name__ == '__main__':
    unittest.main()
