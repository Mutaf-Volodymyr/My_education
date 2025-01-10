-- Подключитесь к базе данных hr (которая находится на удаленном сервере).
USE hr;

-- Выведите количество сотрудников в базе
select count(*)
from employees;

-- Выведите количество департаментов (отделов) в базе
select count(*)
from departments;


-- Подключитесь к базе данных World (которая находится на удаленном сервере).
use world;

-- Выведите среднее население в городах Индии (таблица City, код Индии - IND)

select avg(Population) as avg_pop
from city
where CountryCode = 'IND';

-- Выведите минимальное население в индийском городе и максимальное.
select min(Population), max(Population)
from city
where CountryCode = 'IND';


-- Выведите самую большую площадь территории.
select max(SurfaceArea)
from country;



-- Выведите среднюю продолжительность жизни по странам.

select Name, LifeExpectancy
from country;


-- Найдите самый населенный город (подсказка: использовать подзапросы)
select *
from city
where Population = (
select max(Population)
from city)



