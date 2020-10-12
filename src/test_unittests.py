import pytest
import unittest
from unittest.mock import Mock, patch, call

from src.functions import (
    get_table_width,
    get_dict_table_width,
    print_dict_table,
    print_header,
    print_menu,
    print_separator,
)


class Test_Methods(unittest.TestCase):
    def test_get_table_width(self):

        title = "The long title"
        data = {"1": "here", "text here": "here"}
        expected = 17

        actual = get_table_width(title, data)

        self.assertTrue(actual == expected)

    def test_get_table_width_i(self):

        title_1 = "The"
        data_1 = {"A very long title indeed": "here here"}
        expected_1 = 27

        actual_1 = get_table_width(title_1, data_1)

        self.assertTrue(actual_1 == expected_1)

    @patch("src.functions.get_dict_table_width")
    @patch("src.functions.print_header")
    @patch("src.functions.print_separator")
    @patch("builtins.print")
    def test_print_dict_table(
        self,
        mock_print,
        mock_print_separator,
        mock_print_header,
        mock_get_dict_table_width,
    ):
        # Arrange
        title = "ti"
        data = {1: "22", "second string": "timewarp"}
        mock_get_dict_table_width.return_value = 2

        expected = [call("| 22"), call("| timewarp")]
        # Act
        print_dict_table(title, data)

        # Assert
        mock_get_dict_table_width.assert_called_once_with(title, data)
        mock_print_header.assert_called_once_with(title, 2)
        mock_print_separator.assert_called_once_with(2)

        self.assertEqual(expected, mock_print.call_args_list)

    @patch("builtins.print")
    def test_print_header(self, mock_print):
        # Arrange
        title = "title"
        width = 5

        expected = [call("====="), call(" ", "title"), call("=====")]

        # Act
        print_header(title, width)

        # Assert
        self.assertEqual(expected, mock_print.call_args_list)


if __name__ == "__main__":
    unittest.main()
