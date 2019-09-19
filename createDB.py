import sqlite3

#ESTABLISH CONNECTION
conn = sqlite3.connect('FITARA.db')

#CREATE DB
print ("Opened database successfully");

#EXCECUTE QUERY
conn.execute('CREATE TABLE fit (doc TEXT, prediction REAL)')
print ("Table created successfully")
conn.close()
