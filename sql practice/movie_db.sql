create database movie_db;
use movie_db;
create table movie(
	id int auto_increment primary key,
    tittle varchar(100) null unique,
    language enum("english","malayalam","hindi","tamil") default"malayalam",
    rating float not null,
    run_time_in_minutes int not null,
    director varchar(50) null ,
    genre enum("comedy","thriller","action","horror") default "comedy"
    );
desc movie;

insert into movie(tittle,language,rating,run_time_in_minutes,director,genre)values("sarvam maya","malayalam",5,120,"akhil sathyan","comedy");

insert into movie(tittle,language,rating,run_time_in_minutes,director,genre)values("baahubali","tamil",4.5,120,"rajamouli","action");

insert into movie(tittle,language,rating,run_time_in_minutes,director,genre)values("bouganville","malayalam",4,175,"amal neerad","thriller" );

insert into movie(tittle,language,rating,run_time_in_minutes,director,genre)values("Pk","hindi",4.5,120,"anubav sihna","action" );

select * from movie
    

