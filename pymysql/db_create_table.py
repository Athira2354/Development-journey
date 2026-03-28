from mysql import connector
connection =connector.connect(
    host="localhost",
    user= "root",
    password="Athira@123",
    database="py_db"
    
)
cursor=connection.cursor()
query="""
create table sports(
id int auto_increment primary key,
name varchar(100) not null,
players_count int not null default 1,
country varchar(200) not null
)
"""
cursor.execute(query)
connection.commit()
print("table created")