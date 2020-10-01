from src.functions import print_menu, print_dict_table, print_separator, print_header

import src.functions

import unittest
import pytest
from unittest.mock import Mock, patch, call

class Test_Methods(unittest.TestCase):

  @patch("src.functions.get_dict_table_width")
  @patch("src.functions.print_header")
  @patch("src.functions.print_separator")
  @patch("builtins.print")
  def test_print_dict_table(self, mock_print, mock_print_separator, mock_print_header, mock_get_dict_table_width ):
    #Arrange
    title = "ti"
    data = {1:"22", "headlight":"timewarp"}
    mock_get_dict_table_width.return_value = 2
    
    #Act
    print_dict_table(title, data)

    #Assert
    mock_get_dict_table_width.assert_called_once_with(title, data)
    mock_print_header.assert_called_once_with(title, 2)
    mock_print_separator.assert_called_once_with(2)
    
    expected = [call("| 22"), call("| timewarp")]

    self.assertEqual(expected, mock_print.call_args_list)


if __name__ == "__main__":
    unittest.main()