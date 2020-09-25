import csv
import saving_class
import sys
sys.path.append('/home/bob/gen/Two/sources')
sys.path.append('/home/bob/gen/Two/persistence')

from functions import print_dict_table, print_table, print_header, print_separator, get_dict_table_width, get_table_width, print_menu, get_selection, wait

from classes import Round, Person
#Adding a Comment
people_dict = {}
drinks_dict = {}
favourite_drinks = {}

people_file = open("/home/bob/gen/Two/persistence/people.csv", "r+")
drinks_file = open("/home/bob/gen/Two/persistence/drinks.txt", "r+")

people_lines = people_file.readlines()
drinks_lines = drinks_file.readlines()

try:
    for i, person in enumerate(people_lines):
        person = person.strip()
        
        people_dict[i] = person.split(",")[0]
        print(people_dict[i])

    for i, drink in enumerate(drinks_lines):
        drink = drink.strip()
        drinks_dict[i] = drink

except:
    people_file.close()
    drinks_file.close()

def start_app():
 while True:
    
    print_menu()
    
    try:
        option = int(input("Message here   "))
    except ValueError as e:
        print(e)
        print("This is a helpful message explaining that your input was incorrect")
        exit()
    except Exception:
        print("Something went wrong")
        exit()

    if option == 1:
      people = saving_class.Save_load()
      people.list_csv("people")

    elif option == 2:
        drinks = saving_class.Save_load()
        drinks.list_csv("drinks")

    elif option == 3:
        new_person = saving_class.Save_load()
        new_person.save_to_csv("people")

    elif option == 4:
        new_person = saving_class.Save_load()
        new_person.save_to_csv("drinks")
  


    elif option == 5:
        print("Choose the number that corresponds with the name you wish to select")
      
        for key, value in people_dict.items():
            print(f"{key} {value}")
        person = people_dict[int(input("Enter here "))]
        for key, value in drinks_dict.items():
            print(f"{key} {value}")

        favourite_drinks[person] = drinks_dict[
            int(input("Enter the numerical value of the drink you wish to select "))
        ]

    elif option == 6:
        width = get_dict_table_width("Favourite Drinks", favourite_drinks)
        print_header("Favourite Drinks", width)
       
        for key, value in favourite_drinks.items():
            print(f"| {key} {value}")
        print_separator(width)

        wait()
    
    elif option == 7:
        current_round = Round()
        for key, value in drinks_dict.items():
            print(f"{key} {value}")
        
        current_round.add_to_order(drinks_dict[
            int(input("Enter the numerical value of the drink you wish to add to the round "))
        ])
    
    elif option == 8:
     
      if current_round.size() > 3:
          print("Sorry, too many drinks")
          wait()
      else:
        for key, value in drinks_dict.items():
            print(f"{key} {value}")

        current_round.add_to_order(drinks_dict[
            int(input("Enter the numerical value of the drink you wish to select "))
        ])

    elif option == 9:

        current_round.view_round()
        wait()

    elif option == 11:
        
        print("Thanks for playing")
        people_file.close()
        drinks_file.close()
        exit()

    else:
        print(f'"{option}" is not a recognised command.')
        wait()

if __name__ == "__main__":
    start_app()