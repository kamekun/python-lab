#import de mysql lib from command: pip install mysql-connector-python
import mysql.connector

db = mysql.connector(
  user="",
  password="",
  host="",
  database="",
)

cursor = db.cursor()
cursor.execute("select * from users")
result = cursor.fetchall()

for user in result:
 print(user)

  
