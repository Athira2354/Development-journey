from mysql import connector

connection =connector.connect(
    host="localhost",
    user="root",
    password="Athira@123",
    database="py_db"
)

cursor= connection.cursor()
query=" select * from sports "
cursor.execute(query)
records=cursor.fetchall()
for row in records:
    print(row)
cursor.close()
connection.close()
print("fetched")
