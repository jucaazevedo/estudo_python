import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="suse",
  passwd="Suse#211095"
)

print(mydb) 

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 


mydb2 = mysql.connector.connect(
  host="localhost",
  user="suse",
  passwd="Suse#211095",
  database="suseneomeritor"
)

print(mydb2) 


mycursor = mydb2.cursor()

mycursor.execute("select * from usuario")

linhas = mycursor.fetchall()

print(linhas)
