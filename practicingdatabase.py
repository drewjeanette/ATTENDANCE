import sqlite3
connection = sqlite3.connect ("sampleDB.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM sampleTable WHERE year > 2000")
print(cursor.fetchall())