from src.functions import wait, print_dict_table
import csv

class Round:
  def __init__(self):
      self.list_of_drinks = []
    
  def add_to_order(self, new_drink):
    
      self.list_of_drinks.append(new_drink)
  
  def view_round(self):
      print(self.list_of_drinks)
  
  def size(self):
      return len(self.list_of_drinks)

class Person:

 def __init__(self):
   print("")

 def list_people(self):
     people_dict = {}
     people_list = []
     with open("/home/bob/gen/Two/persistence/people.csv", mode="r") as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
                
                 people_list.append(row[0])

     list_people_loop(people_list)
     print_dict_table("People", people_dict)
     wait()   
          
def list_people_loop(people_list):
       for i, person in enumerate(people_list):
          person = person.strip()
          people_dict[i] = person

def add_person(self):
    people_dict = {}
    people_list = []
    with open("/home/bob/gen/Two/persistence/people.csv", mode="a", newline="") as csvfile:
         new_name = [input("Input here:  "), 18]
         writer = csv.writer(csvfile)
         writer.writerow(new_name)
         wait()
#      for i, person in enumerate(people_list):
#        person = person.strip()
#        people_dict[i] = person

#      print_dict_table("People", people_dict)
#      wait()   

#   people_file = open("people.txt", "r+")
  
#   people_lines = people_file.readlines()
 
#   person_to_add = input("Name here ")
#   people_file.write(f"\n{person_to_add} ")
#   people_file.close()
