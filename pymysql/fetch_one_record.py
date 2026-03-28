from mysql import connector

connection =connector.connect(
    host="localhost",
    user="root",
    password="Athira@123",
    database="py_db"
)

cursor= connection.cursor()
query=" select * from sports where id=%s "
data=(1,)
cursor.execute(query,data)
record=cursor.fetchone()
print(record)
cursor.close()
connection.close()
print("fetched")
