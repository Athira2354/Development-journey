create database diet_db ;
use diet_db ;
create table user(
id int auto_increment primary key,
name varchar(100) not null,
email varchar(100) not null unique,
phone varchar(10) not null unique
);
create table foodlog(
id int auto_increment primary key,
title varchar(150) not null,
meal_type enum("breakfast","lunch","dinner")default "breakfast",
serving_size varchar(200) not null,
calorie int  default 50,
date datetime default current_timestamp,
user_id int not null,
foreign key(user_id) references user(id) on delete cascade
 );
insert into user(name,email,phone)values("vipin","v@gmail.com",7485961234),
("sibin","sib@gmail.com",9685742121);

select * from user ;
update user set name="anu" where id =1 ;
desc foodlog ;
insert into foodlog(title,meal_type,serving_size,calorie,user_id) values("pulav","breakfast","250gm",450,1);
insert into foodlog(title,meal_type,serving_size,calorie,user_id) values("meals","lunch","300gm",500,1);
insert into foodlog(title,meal_type,serving_size,calorie,user_id) values("rice","dinner","250gm",450,1);
select * from foodlog ;

select user.name,foodlog.title,foodlog.calorie from user inner join foodlog on user.id=foodlog.user_id;
select user.name,foodlog.title,foodlog.calorie from user left join foodlog on user.id=foodlog.user_id;