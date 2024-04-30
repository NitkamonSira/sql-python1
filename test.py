import sqlite3
db = sqlite3.connect('something.db')
cursor = db.cursor()
sql = "SELECT * FROM Colour;"
cursor.execute(sql)
results = cursor.fetchall()
# print nicely
for colour in results:
    print(colour)

# close the db
db.close()