# Подключитесь к базе данных world (которая находится на удаленном сервере).
use world;

# общие выборки для удобства
select * from city;
select * from country;
select * from countrylanguage;

# Выведите список стран с языками, на которых в них говорят.
select
    c.Name,
    cl.Language
from world.countrylanguage as cl
inner join world.country as c
    on cl.CountryCode = c.Code;

# Выведите список городов с их населением и названием стран
select
    co.Name as country,
    ci.Name as city,
    ci.Population as populatoin
from city as ci
inner join country as co
on ci.CountryCode = co.Code;

# Выведите список городов в South Africa (если речь о регионе)
select
    ci.Name as city
from city as ci
inner join country as co
on ci.CountryCode = co.Code
and co.Region = 'Southern Africa';

# 4.  ИЛИ Выведите список городов в South Africa
# (если речь о стране ЮАР)

select Name, CountryCode
from world.city
where CountryCode = (
    select Code
    from world.country
    where Name = 'South Africa');

-- Вариант Лены
-- 4. Выведите список городов в South Africa
SELECT city.Name AS city_name, country.Name FROM city
JOIN country ON country.code = city.CountryCode
AND country.Name = 'South Africa';

# Выведите список стран с названиями столиц.
# Подсказка: в таблице country есть поле Capital,
# которое содержит номер города из таблицы City.

select
    w.Name as Country,
    c.Name as Capital
from world.country as w
inner join world.city c
    on w.Capital = c.ID;

# Измените предыдущий запрос таким образом, чтобы выводилось население в столице.
select
    w.Name as Country,
    c.Name as Capital,
    c.Population as Cap_pop
from world.country as w
inner join world.city c
    on w.Capital = c.ID;


-- Или вариант Лены
-- 6. Измените запрос 4 таким образом, чтобы выводилось население в столице.
SELECT country.Name, city.Name, city.Population FROM country
JOIN city ON city.ID = country.Capital
AND country.Name = 'South Africa';

# Напишите запрос, который возвращает название столицы United States
select
    ci.Name
from city as ci
where ID = (
    select Capital from country
    where Name = 'United States');

# Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
use hr;
select
    emp.first_name,
    emp.last_name,
    loc.city
from employees as emp
inner join departments as dep
on emp.department_id = dep.department_id
inner join locations as loc
on dep.location_id = loc.location_id;

# Используя базу hr_data.sql, вывести города и соответствующие городам страны.
select
    l.city as city,
    c.country_name  as country
from locations as l
inner join countries as c
on l.country_id = c.country_id;






