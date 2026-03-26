-- Create Database
CREATE DATABASE penguins_db;

-- Use Database
USE penguins_db;

-- Create Table
CREATE TABLE penguins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    species VARCHAR(50),
    island VARCHAR(50),
    bill_length_mm DECIMAL(5,2),
    bill_depth_mm DECIMAL(5,2),
    flipper_length_mm INT,
    body_mass_g INT,
    sex VARCHAR(10)
);

-- Insert Sample Data (60+ rows)

INSERT INTO penguins 
(species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex)
VALUES

('Adelie','Torgersen',39.1,18.7,181,3750,'Male'),
('Adelie','Torgersen',39.5,17.4,186,3800,'Female'),
('Adelie','Torgersen',40.3,18.0,195,3250,'Female'),
('Adelie','Torgersen',36.7,19.3,193,3450,'Female'),
('Adelie','Torgersen',39.3,20.6,190,3650,'Male'),
('Adelie','Torgersen',38.9,17.8,181,3625,'Female'),
('Adelie','Torgersen',39.2,19.6,195,4675,'Male'),
('Adelie','Torgersen',34.1,18.1,193,3475,'Male'),

('Adelie','Dream',42.0,20.2,190,4250,'Male'),
('Adelie','Dream',37.8,17.1,186,3300,'Female'),
('Adelie','Dream',37.8,17.3,180,3700,'Female'),
('Adelie','Dream',41.1,17.6,182,3200,'Female'),
('Adelie','Dream',38.6,21.2,191,3800,'Male'),
('Adelie','Dream',34.6,21.1,198,4400,'Male'),

('Adelie','Biscoe',39.6,17.7,186,3500,'Female'),
('Adelie','Biscoe',36.5,16.6,181,2850,'Female'),
('Adelie','Biscoe',37.6,19.3,181,3300,'Male'),
('Adelie','Biscoe',35.0,17.9,190,3450,'Female'),

('Chinstrap','Dream',46.5,17.9,192,3500,'Female'),
('Chinstrap','Dream',50.0,19.5,196,3900,'Male'),
('Chinstrap','Dream',51.3,19.2,193,3650,'Male'),
('Chinstrap','Dream',45.4,18.7,188,3525,'Female'),
('Chinstrap','Dream',52.7,19.8,197,3725,'Male'),
('Chinstrap','Dream',45.2,17.8,198,3950,'Female'),

('Gentoo','Biscoe',46.1,13.2,211,4500,'Female'),
('Gentoo','Biscoe',50.0,16.3,230,5700,'Male'),
('Gentoo','Biscoe',48.7,14.1,210,4450,'Female'),
('Gentoo','Biscoe',50.0,15.2,218,5700,'Male'),
('Gentoo','Biscoe',47.6,14.5,215,5400,'Male'),
('Gentoo','Biscoe',46.5,13.5,210,4550,'Female'),

('Gentoo','Biscoe',45.4,14.6,211,4800,'Female'),
('Gentoo','Biscoe',46.7,15.3,219,5200,'Male'),
('Gentoo','Biscoe',43.3,13.4,209,4400,'Female'),
('Gentoo','Biscoe',46.8,15.4,215,5150,'Male'),
('Gentoo','Biscoe',40.9,13.7,214,4650,'Female'),
('Gentoo','Biscoe',49.0,16.1,216,5550,'Male'),

('Adelie','Dream',38.1,17.0,181,3175,'Female'),
('Adelie','Dream',37.5,18.9,179,2975,'Female'),
('Adelie','Dream',35.7,16.9,185,3150,'Female'),

('Chinstrap','Dream',49.6,18.2,193,3775,'Male'),
('Chinstrap','Dream',50.8,19.0,210,4100,'Male'),

('Gentoo','Biscoe',48.2,14.3,210,4600,'Female'),
('Gentoo','Biscoe',49.5,16.2,229,5800,'Male'),

('Adelie','Biscoe',38.2,18.1,185,3950,'Male'),
('Adelie','Biscoe',37.3,16.8,192,3000,'Female'),

('Chinstrap','Dream',47.0,17.5,187,3400,'Female'),
('Chinstrap','Dream',48.5,18.0,195,3900,'Male'),

('Gentoo','Biscoe',44.5,14.7,214,4700,'Female'),
('Gentoo','Biscoe',50.5,15.9,225,5550,'Male');

desc penguins ;
select * from penguins ;
select count(*) from penguins ;
select distinct(species) from penguins ;
select distinct island from penguins;
select *  from penguins where sex= "Male" ;
select * from   penguins where body_mass_g >4000 ;
-- LEVEL 2: INTERMEDIATE (WHERE + FILTER) 
-- 6. Penguins from island ‘Biscoe’
  select * from penguins where island="Biscoe";
-- 7. Penguins with flipper_length_mm > 200
select * from penguins where flipper_length_mm>200;
-- 8. Penguins with bill_length between 40 and 50 
select * from penguins where bill_length_mm >40 and bill_length_mm< 50 ;
-- 9. Female penguins with body mass < 3500 
select * from penguins where sex= "Female" and body_mass_g<3500 ;
-- 10. Penguinswhere species = ‘Adelie’ AND island = ‘Dream’
select * from penguins where species ="Adelie" and island ="Dream";
-- LEVEL 3: AGGREGATE FUNCTIONS 
-- 11. Average body mass 
select avg(body_mass_g) as avg_body_mass from penguins;
-- 12. Maximum flipperlength 
select max(flipper_length_mm) as max_flipper_length from penguins ;
-- 13. Minimum bill depth 
select min(bill_length_mm) as min_bill_length from penguins ;
-- 14. Total number of records 
select count(*) from penguins ;
-- 15. Total bodymass of all penguins
select sum(body_mass_g) as sum_bodymass from penguins ;
-- LEVEL 4: GROUP BY 
-- 16. Average body mass by species 
select species,avg(body_mass_g) as avg_body_mass_g from penguins group by species ;
-- 17. Count penguin sper island 
select island,count(*) as penguins_count from penguins group by island;
-- 18. Average flipper length by sex 
select sex,avg(flipper_length_mm) as avg_flipper_length from penguins group by sex;
-- 19. Average bill length byspecies 
select species,avg(bill_length_mm) as avg_bill_length from penguins group by species;
-- 20. Total body mass per island
select island , sum(body_mass_g) as total_body_mass_g from penguins group by island;

-- LEVEL 5: GROUP BY + HAVING 
-- 21. Species with avg body mass > 4000 
select species,avg(body_mass_g) as avg_body_mass_g  from penguins group by species having avg(body_mass_g) >4000 ;
-- 22.Islands with more than 10 penguins
select island,count(*) as penguin_count from penguins group by island having count(*) > 10;
-- 23. Groups with avg flipper length >200 
select sex,avg(flipper_length_mm) as avg_flipper_length from penguins group by sex having avg(flipper_length_mm) > 200;
-- 24. Species with count > 5
select species,count(*) as species_count from penguins group by species having count(*) > 5;
-- 25. Islands with avg body mass < overall avg
select  island,avg(body_mass_g) as avg_body_mass from penguins group by island having avg(body_mass_g) < (select avg(body_mass_g)from penguins );

-- LEVEL 6: SUBQUERIES 
-- 26. Penguins heavier than average
select * from penguins where body_mass_g > (select avg(body_mass_g) from penguins);
-- 27. Penguin withmaximum body mass 
select * from penguins where body_mass_g = ( select max(body_mass_g)from penguins);
-- 28. Penguins with flipper length less than average
select * from penguins where flipper_length_mm < (select avg(flipper_length_mm)from penguins);
-- 29.Species whose avg body mass > overall avg
 select species,avg(body_mass_g) as avg_body_mass from penguins group by species having  avg(body_mass_g) > (select avg(body_mass_g) from penguins);
-- 30. Penguins heavier than their species average (correlated)

-- LEVEL 7: ADVANCED DATA ANALYST 
-- 31. Find top 3 heaviest penguins 
-- 32. Findspecies with highest avg body mass 33. Rank penguins by body mass 
-- 34.Find difference between max and avg body mass per species 
-- 35. Findpercentage contribution of each species count
