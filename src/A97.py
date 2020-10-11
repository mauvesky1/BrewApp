import csv
import src.saving_class as saving_class
import sys
sys.path.append('/home/bob/gen/Two/sources')
sys.path.append('/home/bob/gen/Two/persistence')

from src.functions import print_dict_table, print_table, print_header, print_separator, get_dict_table_width, get_table_width, print_menu, get_selection, wait

from src.classes import Round, Person

def start_app():
 while True:
    
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
      people = saving_class.Save_load()
      #people.list_csv("people")
      people.list_from_database("person")

    elif option == 2:
        drinks = saving_class.Save_load()
        #drinks.list_csv("drinks")
        drinks.list_from_database("drink")

    elif option == 3:
        new_person = saving_class.Save_load()
        #new_person.save_to_csv("people")
        new_person.save_to_database("persons")

    elif option == 4:
        new_person = saving_class.Save_load()
        #new_person.save_to_csv("drinks")
        new_person.save_to_database("drinks")

    elif option == 5:
        new_interaction = saving_class.Save_load()
        new_interaction.choose_favourite_drink()

    elif option == 6:
        new_interaction = saving_class.Save_load()
        width = get_dict_table_width("Favourite Drinks", favourite_drinks)
        print_header("Favourite Drinks", 19 )
       
        new_interaction.view_favourite_drinks()
        # for key, value in favourite_drinks.items():
        #     print(f"| {key} {value}")
        print_separator(19)

        wait()
    
    elif option == 7:
        new_interaction = saving_class.Save_load()
        new_interaction.new_round()
        # current_round = Round()
        # for key, value in drinks_dict.items():
        #     print(f"{key} {value}")
        
        # current_round.add_to_order(drinks_dict[
        #     int(input("Enter the numerical value of the drink you wish to add to the round "))
        # ])
    
    elif option == 8:
        new_interaction = saving_class.Save_load()
        new_interaction.order_saved_round()
     

    elif option == 9:
        new_interaction = saving_class.Save_load()
        new_interaction.order_favourite_round()

        

    elif option == 11:
        
        print("Thanks for playing")
        exit()

    else:
        print(f'"{option}" is not a recognised command.')
        wait()

if __name__ == "__main__":
    start_app()