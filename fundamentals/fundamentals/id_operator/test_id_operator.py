import unittest


class IdOperatorTest(unittest.TestCase):

    def test_id_operator_should_return_same_value_for_same_integer_object(self):
        # given
        x = (1, 53)
        y = (1, 53)
        z = (99, 1)

        # when
        x_first_item_and_y_first_item_have_same_id = x[0] is y[0]
        y_first_item_and_z_last_item_have_same_id = y[0] is z[1]
        x_first_item_and_y_first_item_are_same_object = x[0] == y[0]
        y_first_item_and_z_last_item_are_same_object = y[0] == z[1]

        # then
        self.assertTrue(x_first_item_and_y_first_item_have_same_id)
        self.assertTrue(y_first_item_and_z_last_item_have_same_id)
        self.assertTrue(x_first_item_and_y_first_item_are_same_object)
        self.assertTrue(y_first_item_and_z_last_item_are_same_object)


if __name__ == '__main__':
    unittest.main()
