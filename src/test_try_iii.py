from functions import print_menu, print_dict_table


import unittest
from unittest.mock import Mock, patch, call

class Test_Methods(unittest.TestCase):

  @patch("functions.get_dict_table_width")
  def print_dict_table(title, data, mock_get_dict_table_width):
    width = get_dict_table_width(title, data)
    print_header(title, width)
    for value in data.values():
        print(f"| {value}")
    print_separator(width)




if __name__ == "__main__":
    unittest.main()