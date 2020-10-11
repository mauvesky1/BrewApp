import csv
import src.saving_class as saving_class
import sys
sys.path.append('/home/bob/gen/Two/sources')
sys.path.append('/home/bob/gen/Two/persistence')

from src.functions import print_dict_table, print_table, print_header, print_separator, get_dict_table_width, get_table_width, print_menu, get_selection, wait

from src.classes import Round, Person

def start_app():
 while True:
    new_interaction = saving_class.Save_load()
    print_menu()
    
    try:
        option = int(input("Message here   "))
    except ValueError as e:
        print(e)
        print("This is a helpful message explaining that your input must be one of the numbers indicating a menu option")
        option =  int(input("Message here   "))
    except Exception:
        print("Something went wrong")
        exit()

    if option == 1:
     
      new_interaction.list_from_database("person")

    elif option == 2:
      
        new_interaction.list_from_database("drink")

    elif option == 3:
        
        new_interaction.save_to_database("persons")

    elif option == 4:
       
        new_interaction.save_to_database("drinks")

    elif option == 5:
       
        new_interaction.choose_favourite_drink()

    elif option == 6:
        width = get_dict_table_width("Favourite Drinks", {})
        print_header("Favourite Drinks", 19 )
       
        new_interaction.view_favourite_drinks()

        print_separator(19)
        wait()
    
    elif option == 7:
        new_interaction.new_round()

    elif option == 8:
        new_interaction.order_saved_round()

    elif option == 9:
        new_interaction.order_favourite_round()    

    elif option == 11:
        
        print("Thanks for playing")
        exit()

    else:
        print(f'"{option}" is not a recognised command.')
        wait()

if __name__ == "__main__":
    start_app()