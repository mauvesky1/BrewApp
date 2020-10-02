import csv
import pymysql

from src.functions import print_dict_table, wait

#this class can load a list of data from a csv and save to csv

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
    
    connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
    cursor = connection.cursor()
    persons = {}

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
    print(table_selector)
    connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
    cursor = connection.cursor()
    new_name = [input("Input here:  ")]

    cursor.execute(f"INSERT INTO {table_selector}(name) VALUES(%s)", new_name)
    connection.commit()
    
  
    cursor.close()
   
    #print(persons)
    wait()

  def choose_favourite_drink(self):
    print("Choose the number that corresponds with the name you wish to select")

    connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
    cursor = connection.cursor()
    #persons = {}

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
