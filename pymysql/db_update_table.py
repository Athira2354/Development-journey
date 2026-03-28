from mysql import connector


connection =connector.connect(
    host="localhost",
    user="root",
    password="Athira@123",
    database="py_db"
)
cursor=connection.cursor()
query="update sports set name=%s where id=%s"
data=("t-20",1)

cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("data inserted")
