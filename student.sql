-- line comment
-- query for listing all database
show databases ;
-- query for creating database
create database student_db;
--  to use database
use student_db ;
-- query for creating student rable
-- student[id,name,course,email,place,age]
create table student (
id int auto_increment primary key,
name varchar(70) not null,
course enum("django","mernstack","asp.net")default "django",
place varchar(100) not null,
age int not null,
email varchar(90) unique not null
);
desc student ;
insert into student(id,name,course,place,age,email)values(100,"Akhil","django","thrissur",28,"akhil#123@gmail.com" )

insert into student(id,name,course,place,age,email)values(101,"Amal","asp.net","thrissur",25,"amal@gmail.com" )

insert into student (id,name,course,place,age,email)values(102,"Amay","mernstack","thrissur",25,"amay@gmail.com" )

select * from student

select name,course from student

-- display student details whose place = thrissur
select * from student where  place = "thrissur" ;

select * from student where course= "django" ;

-- display thrissur django student

select * from student where place="thrissur" and course ="django";

-- age greater than 30

select * from student where age > 25;


