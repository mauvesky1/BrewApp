import src.saving_class as saving_class
#NOTE: Hi, this is a test addition
from src.functions import (
    get_selection,
    get_table_width,
    print_dict_table,
    print_table,
    print_header,
    print_separator,
    print_menu,
    wait,
)


def start_app():
    while True:
        new_interaction = saving_class.Save_load()
        print_menu()

        try:
            option = int(input("Message here   "))
        except ValueError as e:
            print(e)
            print(
                "This is a helpful message explaining that your input must be one of the numbers indicating a menu option"
            )
            option = int(input("Message here   "))
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
            print_header("Favourite Drinks", 19)
            new_interaction.view_favourite_drinks()
            print_separator(19)
            wait()

        elif option == 7:
            new_interaction.new_round()

        elif option == 8:
            new_interaction.order_saved_round()

        elif option == 9:
            new_interaction.order_favourite_round()

        elif option == 10:

            print("Thanks for viewing")
            exit()


if __name__ == "__main__":
    start_app()