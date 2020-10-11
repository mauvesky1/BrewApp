import csv
import pymysql

from src.functions import print_dict_table, get_table_width, wait

class Save_load:
  def __init__(self):
    print("")

  def list_csv(self, filepath):
    
     dict_to_print = {}
  
     csv_list = []
     with open(f"/home/bob/gen/Two/persistence/{filepath}.csv", mode="r") as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
                
                 csv_list.append(row[0])

     for i, person in enumerate(csv_list):
       person = person.strip()
       dict_to_print[i] = person

     print_dict_table(filepath.title(), dict_to_print)
     wait()   

  def save_to_csv(self,filepath):
   
    people_dict = {}
    people_list = []
    with open(f"/home/bob/gen/Two/persistence/{filepath}.csv", mode="a", newline="") as csvfile:
         new_name = [input("Input here:  ")]
         writer = csv.writer(csvfile)
         writer.writerow(new_name)
         wait()

  def list_from_database(self, table_selector):
     
    try:
       connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
       cursor = connection.cursor()
       persons = {}

    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()

    cursor.execute(f"SELECT {table_selector}_id, name from {table_selector}s")
    connection.commit()
    rows = cursor.fetchall()
    for row in rows:
    
      persons[row[0]] = row[1] 
  
    cursor.close()
    print_dict_table("title", persons)
    #print(persons)
    wait()
  
  def save_to_database(self, table_selector):
    try:
      print(table_selector)
      connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
      cursor = connection.cursor()

    except RuntimeError as e:
      print("Runtime ERROR, is the database up?", e)
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    new_name = [input("Input here:  ")]

    cursor.execute(f"INSERT INTO {table_selector}(name) VALUES(%s)", new_name)
    connection.commit()
    
  
    cursor.close()
   
    #print(persons)
    wait()

  def choose_favourite_drink(self):
    print("Choose the number that corresponds with the name you wish to select")
    try:
      connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
      cursor = connection.cursor()
    
    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    cursor.execute(f"SELECT person_id, name from persons;")
    #connection.commit()
    rows = cursor.fetchall()
    for row in rows:
    
      print(row[0], ":", row[1]) 
      
    selection = int(input("Enter here: "))
    cursor.execute(f"SELECT drink_id, name from drinks")
    connection.commit()
    rows = cursor.fetchall()
    for row in rows:
    
      print("| ", row[0], ":", row[1]) 
    
    print("Select favourite drink: ")
    drink_selection = int(input("Enter here: "))
    args = [selection, drink_selection]
    cursor.execute(f"UPDATE persons SET favourite_drink = {drink_selection} where person_id = {selection}")
    connection.commit()
    cursor.close()
    
    wait()

  def view_favourite_drinks(self):
     
    people_list = []
    drinks_list = []
   
    try:
      connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
      cursor = connection.cursor()
    
    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    cursor.execute(f"SELECT name, favourite_drink from persons;")
   
    connection.commit()

    rows = cursor.fetchall()
    for row in rows:
       people_list.append(row[0])
       drinks_list.append(row[1])
    #print(people_list, drinks_list)
    
    cursor.execute(f"SELECT drink_id, name from drinks;")
    connection.commit() 
    rows = cursor.fetchall()
   
    drinks_dict = {}
    for a,b in rows:
       #print(b)
       
       drinks_dict[a] = b

    # Turn tupales into dictionary
    #Replace drinks list with items from dictionary
    for i, drink in enumerate(drinks_list):
       if drink == None:
          drink = 0
       drinks_list[i] = drinks_dict[drink]
    
    #favourite_drinks_dict = dict(zip(people_list, drinks_list))[drink]
    
    favourite_drinks_dict = dict(zip(people_list, drinks_list))
    #print(favourite_drinks_dict)
    for row in favourite_drinks_dict.items():
      print("|", row[0]," : ", row[1])
    #print(favourite_drinks_dict.items())

    cursor.close()
  
  def new_round(self):
    
    print("Choose the number that corresponds with the person you wish to be the round owner.")
    try:
        connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
        cursor = connection.cursor()
    
    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    cursor.execute(f"SELECT person_id, name from persons;")
    #connection.commit()
    rows = cursor.fetchall()
    for row in rows:
    
      print(row[0], ":", row[1]) 
      
    round_owner_id = int(input("Enter here: "))

    cursor.execute(f"SELECT drink_id, name from drinks;")
    #connection.commit()
    rows = cursor.fetchall()
    print("\nPress 0 to exit. \nList of Drinks:")
    for row in rows[1:]:
    
      print(row[0], ":", row[1]) 

    
    drinks_list = [round_owner_id] 
    print("")
    while True:
      selected_drink = int(input("Please select a drink to add to the round:"))
      if len(drinks_list) > 5:
        print("Sorry, the round is full")
        break
      if selected_drink == 0:
       break
      else:
         drinks_list.append(selected_drink)
    
    drinks_names = []

    print("Your round has been ordered and saved. It consisted of:")
    for drink in drinks_list[1:]:
      for tupale in rows:
        if tupale[0] == drink:
          print(tupale[1]) 
      #print("looing here", drink)
    
    #Santise inputs
    cursor.execute(f"UPDATE persons SET round='{drinks_list}' WHERE person_id={round_owner_id}")
    connection.commit()
    cursor.close()
   
    #print(persons)
    wait()

  def order_saved_round(self):
    try:
        connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
        cursor = connection.cursor()
    
    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    cursor.execute(f"SELECT name, round from persons;")
    #connection.commit()
    rows = cursor.fetchall()
    #print(rows)
    print("Whose round do you wish to order?")
    for i,row in enumerate(rows):
      print((i+1),row[0])
    
    selection = int(input("Select the number corresponding with the person whose round you wish to select: "))
    selected_round = []
    printing_list = []
    
    print("You have ordered:")
    for i,row in enumerate(rows):
      
      if i+1 == selection:
        
        selected_round = eval(row[1])
    
    cursor.execute(f"SELECT drink_id, name from drinks;")
    rows = cursor.fetchall()
    #print(rows)
    for drink in selected_round:
      for row in rows:
        
        if drink == row[0]:
          
          printing_list.append(row[1])
          
    for item in printing_list:
      print(item)
  
    #connection.commit()
    cursor.close()
    wait()
  
  def order_favourite_round(self):
    favourite_drinks_list = []
    print_drinks_list = []
    try:
      connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
      cursor = connection.cursor()
      
    except RuntimeError as e:
      print("Runtime ERROR, is the database up?")
      wait()
    except:
        print("Something went wrong\n", e)
        cursor.close()
        exit()

    cursor.execute(f"SELECT favourite_drink from persons;")
    rows = cursor.fetchall()
    for row in rows:
      if row[0] != None:
        favourite_drinks_list.append(row[0])
    
    cursor.execute(f"SELECT drink_id, name from drinks;")
    rows = cursor.fetchall()
   

    for drink in favourite_drinks_list:
      for row in rows:
        if drink == row[0]:
          print_drinks_list.append(row[1])
          break

    print("Every regular has had their favourite drink ordered!\nThe following drinks have been ordered: ")
    for drink in print_drinks_list:
      print(drink)
   
    cursor.close()
    wait()