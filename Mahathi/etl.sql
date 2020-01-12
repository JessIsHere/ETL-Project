-- table from countries.csv imported

drop table if exists countries

create table if not exists countries(country_id serial primary key,country_name varchar,country_code varchar)

select * from countries
-----------------------------------------------------------------------------------------------------------------------------

drop table if exists country_income

--create table if not exists 
--country_income(countrycode varchar ,incomelevel varchar,foreign key(countrycode) references countries(country_code))

--- table filled from data frame

select * from country_income 

alter table country_income 
add column country_id serial primary key
-------------------------------------------------------------------------------------------------------------------------------

-------table from dataframe

select * from global_traffiking group by Gender

select * from global_traffiking

select Gender from global_traffiking

select count(Gender) from global_traffiking group by Gender

alter table global_traffiking 
add column country_id serial primary key