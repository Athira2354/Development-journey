create database road_db ;
use road_db ;
create table road_issues(
id int auto_increment primary key,
title varchar(150) not null,
issue_type enum("pothole","signal","drainage","lighting","road_damage") default "pothole",
location varchar(150) not null,
severity enum("low","medium","high") default "low",
reported_by varchar(100),
reported_date date,
status enum("open","in_progress","resolved") default "open");
desc road_issues ;
insert into road_issues 
(title, issue_type, location, severity, reported_by, reported_date, status)
values
('Large pothole near bus stop', 'pothole', 'Anna Nagar', 'high', 'Ravi Kumar', '2026-03-20', 'open'),

('Traffic signal not working', 'signal', 'T Nagar', 'medium', 'Priya Sharma', '2026-03-18', 'in_progress'),

('Waterlogging after rain', 'drainage', 'Velachery', 'high', 'Suresh Babu', '2026-03-15', 'open'),

('Street lights not functioning', 'lighting', 'Adyar', 'medium', 'Meena Iyer', '2026-03-10', 'resolved'),

('Cracked road surface', 'road_damage', 'OMR Road', 'low', 'Arjun Nair', '2026-03-12', 'in_progress'),

('Multiple potholes on main road', 'pothole', 'Tambaram', 'high', 'Karthik R', '2026-03-19', 'open'),

('Faded traffic signal lights', 'signal', 'Guindy', 'low', 'Anita Das', '2026-03-17', 'resolved'),

('Blocked drainage causing overflow', 'drainage', 'Perungudi', 'medium', 'Vikram Singh', '2026-03-14', 'in_progress'),

('Broken street lamp', 'lighting', 'Besant Nagar', 'low', 'Divya Menon', '2026-03-11', 'open'),

('Damaged road with uneven surface', 'road_damage', 'Porur', 'medium', 'Rahul Verma', '2026-03-16', 'resolved');


-- 1.display all records
select * from road_issues ;

-- 2. display all road issues
select issue_type from road_issues;

-- 3. Display only title and location 
select title,location from road_issues ;


-- 4 .Show all issues reported in Thrissur 
select * from road_issues where location = "Tambaram" ;


-- 5. Show all pothole issues

select  * from road_issues where issue_type="pothole" ;

-- 6.Show issues with high severity
select issue_type,severity from road_issues where severity="high" ;

-- conditions
-- 7. Display issues where status is open 
select issue_type ,status from road_issues where status= "open";

-- 8. Display issues where severity is medium AND location is Kochi
select issue_type,severity from road_issues where severity="high" and location="Tambaram";

-- 9. Display issues where severity is high OR status is open
select issue_type ,severity, status from road_issues where severity="high" or status= "open" ;

-- 10. Display issues reported after 2026-03-10 10

select issue_type,reported_date from road_issues  where reported_date > 2026-03-10  ;

-- 11.Display issues where status is not resolved
select issue_type,status from road_issues where status ="resolved";

-- like operator
-- 12.Find issues where title starts with “"S"
select * from road_issues where title like "S%" ;

-- 13. Find issues where title ends with “ing”
select * from road_issues where title like '%ing' ;

-- 14 Find issues where location contains “chi” 
select * from road_issues where location like '%Tam%' ;

-- 15.Find reported_by names starting with “a”
select * from road_issues where reported_by like 'a%';

-- 16.Find titles with exactly 5 characters
select * from road_issues where length(title) = '__________';

-- sorting and limiting
-- 17. Display all issues ordered by reported_date(latest first) 
 select * from road_issues order by reported_date desc ;
 
 -- 18. Display top 3 latest issues
 select * from road_issues order by reported_date desc limit 3;
 
 -- 19.Display 2 records after skipping first 3
select * from road_issues order by reported_date desc limit 3, 2;

-- aggregate functions
-- 20.find total no of issues 
select count(*) from road_issues ;
-- 21.Find number of issues in Thrissur 21
select count(*) from road_issues where location="Tambaram" ;
-- 22. Find latest reported date
select max(reported_date) as latest_date from road_issues;

-- 23.. Find earliest reported date
select min(reported_date) as earliest_date from road_issues;

-- 24.Update status to resolved where id = 2
update road_issues set status = 'resolved' where id = 2;
-- 25.Change severity to high for all pothole issues
update road_issues set severity ="high" where issue_type="pothole" ;


 















 


