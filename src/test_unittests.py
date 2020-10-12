from src.functions import (
    print_dict_table,
    get_table_width,
    get_dict_table_width,
    print_header,
    print_separator,
)

import unittest
from unittest.mock import Mock, patch, call

from src.classes import Round


class Test_Methods(unittest.TestCase):
    def test_get_table_width(self):

        title = "The long title"
        data = {"1": "here", "text here": "here"}
        expected = 17

        actual = get_table_width(title, data)

        self.assertTrue(actual == expected)
        print("test_get_table_width")

    def test_get_table_width_i(self):

        title_1 = "The"
        data_1 = {"A very long title indeed": "here here"}
        expected_1 = 27

        actual_1 = get_table_width(title_1, data_1)

        self.assertTrue(actual_1 == expected_1)

        print("test_get_table_width_1")

    def test_round_class(self):

        # Arrange
        new_round = Round()

        expected = []
        # Actual
        actual = new_round.list_of_drinks
        # Assert
        self.assertTrue(actual == expected)
        print("test_round_class")

    def test_round_class_i(self):
        # arrange
        new_round = Round()
        new_drink = "Cola"
        expected = [new_drink]
        # act
        new_round.add_to_order(new_drink)
        actual = new_round.list_of_drinks
        # assert
        self.assertTrue(actual == expected)
        print("test_round_class_i")


if __name__ == "__main__":
    unittest.main()