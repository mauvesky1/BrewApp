from functions import print_dict_table, get_table_width, get_dict_table_width, print_header, print_separator

#from functions import select menu option

def selection_option_from_menu(message, data):
  print_menu(message,data)
  counter_num = get_menu_input("Ener")
  if not validate_menu_input(counter_num, data):
    return False

  return data[count_num -1]

import unittest
from unittest.mock import Mock, patch, call

from classes import Round

class Test_Methods(unittest.TestCase):

  @patch("print_menu")
  @patch("get_menu_input")
  @patch("functions.select_option_from_menu")
  def test_when__number_is_redturned_from_select_retn_the_person_at_that_position(self, mock_validate_menu_input, mock_get_menu_input,  mock_print_menu ):
   #Arrange
   # Make mock msg
   message = "name"
   #make data
   data = ["list", "of","strings"]
   mock_get_menu_input.return_value =  3
   mock_validate_menu_input.return_value = True
   expected = "12"
  #patch print menu , get menu input , validate menu input
   #Act
   actual = select_option_from_menu["of"]
   #Assert
   #self.assertEqual(actual,  data[1])


if __name__ == "__main__":
    unittest.main()