drop table if exists countries_list

Create table if not exists countries_list(country_name varchar,country_code varchar primary key)

select * from countries_list

insert into countries_list values('m','ABW')


drop table if exists countries

create table if not exists countries(country_name varchar,country_code varchar primary key)

select * from countries