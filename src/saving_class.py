import csv
from functions import print_dict_table, wait

#this class cans save to a csv


#this class can load a list of data from a csv


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
