import pymysql

def main():
  connection = pymysql.connect(host ="localhost", port = 33066, user = "root", password = "password", db = "brew_app")
  cursor = connection.cursor()
  args = ("Sall")

  persons = {}
  #cursor.execute("INSERT INTO persons (name) VALUES(%s)",args)
  cursor.execute("SELECT * from persons")
  connection.commit()
  rows = cursor.fetchall()

  for row in rows:
    
    persons[row[0]] = row[1] 
  
  cursor.close()
  print(persons)
  connection.close()


if __name__ == "__main__":
    main()


