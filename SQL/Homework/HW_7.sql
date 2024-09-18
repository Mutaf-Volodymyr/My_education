
# Подключитесь к базе данных hr (которая находится на удаленном сервере).

use hr;

# Выведите количество сотрудников в базе

select count(employees.last_name)
from employees;

# Выведите количество департаментов (отделов) в базе
select count(department_name)
from departments;

# Подключитесь к базе данных World (которая находится на удаленном сервере).
use world;

# Выведите среднее население в городах Индии (таблица City, код Индии - IND)

select avg(Population)
from city
where CountryCode = "IND";

# Выведите минимальное население в индийском городе и максимальное.
select Name, Population as min_max_population
from city
where CountryCode = "IND" and Population = (
    select max(Population)
from city
where CountryCode = "IND"
    ) or Population = (
    select min(Population)
from city
where CountryCode = "IND");


# Выведите самую большую площадь территории.

select Name, SurfaceArea
from country
where SurfaceArea = (
    select max(SurfaceArea)
    from country);
-- учитывая что поле с территорией есть только в таблице country,
-- я решил сделать запрос, который выдает максимальную площадь континента

select Continent, sum(SurfaceArea) as Surface
from country
group by Continent
order by Surface desc
limit 1;

# Выведите среднюю продолжительность жизни по странам.
-- вот тут я вообще не понял вопроса, она же и так указана по странам. Давайте сделаем по региону
select Region, avg(LifeExpectancy)
from country
group by Region;

# Найдите самый населенный город (подсказка: использовать подзапросы)
select concat('в городе ', ci.Name) as a, concat('что в стране ', co.Name) as b, concat('проживает ', ci.Population, ' человек') as c
from city ci
inner join country as co
on ci.CountryCode = co.Code
where ci.Population = (
    select max(Population)
    from city);


