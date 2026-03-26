create database Todo_db ;
use Todo_db;
create table user(
id int auto_increment primary key,
name varchar(200) not null,
email varchar(250) not null unique,
phone varchar(10) not null unique 
);
desc user;
create table task(
id int not null primary key,
title varchar(150) not null,
user_id int not null,
status enum("completed","pending") default "pending",
date datetime default current_timestamp,
foreign key(user_id) references user(id) on delete  cascade

);
desc task;