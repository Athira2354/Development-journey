from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="Athira@123"

)
cursor=connection.cursor()
query="""
create table vehicle(
id int auto_increment primary key,
name varchar(100) not null,
model varchar(100) not null,
running_km  int not null,
fuel_type varchar(100) ,
owner_name varchar(100) not null,
place varchar(100) not null,
owner_id int not null unique,
foreign key(owner_id)references owner(owner_id)
)
"""
cursor.execute(query)
connection.commit()
print("table created")