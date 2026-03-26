create database shopwise_db ;
use shopwise_db ;

create table brand(
id int  auto_increment primary key,
name varchar(150)not null
);
create table product(
id int  auto_increment primary key,
title varchar(200) not null,
price int not null,
brand_id int not null,
foreign key(brand_id) references brand(id) on delete cascade
);
desc product ;

insert into brand(name)values("vanheusan");
insert into brand(name)values("Puma");
insert into brand(name)values("Addidas");
select * from brand ;

insert into product(title,price,brand_id)values("shirt",1200,2);
insert into product(title,price,brand_id)values("sketchers",1200,2);
insert into product(title,price,brand_id)values("trackpants",1200,2);
insert into product(title,price,brand_id)values("trackpants",1200,1);
insert into product(title,price,brand_id)values("tshirt",1200,3);

select * from product ;

select brand.name,product.title,product.price from brand inner join product on brand.id=product.brand_id ;
select brand.name,product.title,product.price from brand left join product on brand.id=product.brand_id ;




