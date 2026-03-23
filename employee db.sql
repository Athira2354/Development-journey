create database employee_db ;

use employee_db;

create table employee (
id int primary key auto_increment,
name varchar(90) not null,
department varchar(90),
salary int not null,
email varchar(100) unique not null

);

insert into employee(name,department,salary,email)value("akhil","full stack developer",35000,"akhil#2@gmail.com");
insert into employee(name,department, salary, email)value("John Smith", "HR", 45000, "john.smith@example.com");
insert into employee(name, department, salary, email)value("Emma Johnson", "Finance", 60000, "emma.johnson@example.com");
insert into employee(name, department, salary, email)value("Michael Brown", "IT", 75000, "michael.brown@example.com");
insert into employee(name, department, salary, email)value("Sophia Davis", "Marketing", 52000, "sophia.davis@example.com");
insert into employee(name, department, salary, email)value("Daniel Wilson", "Sales", 48000, "daniel.wilson@example.com");
insert into employee(name, department, salary, email)value("Olivia Taylor", "IT", 82000, "olivia.taylor@example.com");
insert into employee(name, department, salary, email)value("James Anderson", "Finance", 67000, "james.anderson@example.com");
insert into employee(name, department, salary, email)value("Isabella Thomas", "HR", 46000, "isabella.thomas@example.com");

desc employee;

select * from employee ;

select name,salary from employee ;

-- Display all employees who work in the IT department.
select * from employee where department ="IT" ;

-- Display employees whose name starts with the letter ‘A’.
select * from employee where name like "a%" ;

-- Display employees whose email ends with ‘gmail.com’.
select * from employee where email like "%@gmail.com";

-- Display employees who belong to either HR or Finance department.
select * from employee where department ="HR" or "IT";
-- Display all employees sorted by salary in ascending order.
select * from employee order by salary asc ;

--  Display employees whose salary is between 30000 and 45000.
select * from employee where salary >30000 and salary<45000 ;

select * from employee order by salary desc limit 3 ;

-- ofset is used to skip
select * from employee order by salary desc limit 1  offset 2;




-- AGGREGATE FUNCTION (sum,min,max,average,count)
select max(salary) as max_salary from employee ;
select min(salary) as min_salary from employee ;
select avg(salary) as avg_salary from employee ;

select count(*) from employee ;
select sum(salary) from employee;

-- update akhils department as it

-- update table_name set condition= value where condition
update employee set department="IT",salary=40000 where id =1 ;

delete from employee where id=11 ;


-- Display employees whose name contains exactly 5 characters.
select * from employee where name like "_____";
-- employee with highest salary

-- nested query









