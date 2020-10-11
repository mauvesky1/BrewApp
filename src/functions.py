MENU = """Welcome to list manager!
Please select a list:
[1] People 
[2] Drinks 
[3] Add a person
[4] Add a drink
[5] Choose favourite drink
[6] View favourite drinks
[7] Order next round of drinks
[8] Order Saved Round
[9] Order Everyone a round
[11] Exit
"""
 
def print_dict_table(title, data):
    width = get_dict_table_width(title, data)
    print_header(title, width)
    for value in data.values():
        print(f"| {value}")
    print_separator(width)


def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f"| {item}")
    print_separator(width)


def print_header(title, width):
    print("=" * width)
    print(" ", title)
    print("=" * width)


def print_separator(width):
    print(f"+{'=' * width}")


def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 3
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing


def get_dict_table_width(title, data):
    longest = len(title)
    additional_spacing = 3
    for value in data.values():
        if len(value) > longest:
            longest = len(value)
    return longest + additional_spacing


def print_menu():
    print(MENU)


def get_selection(message):
    return int(input(f"{message}"))


def wait():
    input("Please press Enter to return to the menu ")
