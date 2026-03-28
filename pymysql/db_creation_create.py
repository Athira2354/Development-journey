from mysql import connector

connection =connector.connect(
    host="localhost",
    user="root",
    password="Athira@123"
)
cursor=connection.cursor()
query="create database py_db"
cursor.execute(query)
connection.commit()
print("completed")

