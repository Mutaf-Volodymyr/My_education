-- Подключиться к базе данных world
use world;

-- Вывести население в каждой стране. Результат содержит два поля: CountryCode, sum(Population).
-- Запрос по таблице city.
select Name, Population
from country;

select CountryCode, sum(Population)
from city
group by CountryCode;


-- Изменить запрос выше так, чтобы выводились только страны с
-- населением более 3 млн человек.
select CountryCode, sum(Population) as res
from city
group by CountryCode
having res > 3000000;


-- Сколько всего записей в результате?
# 59
select count(*)
from (
    select CountryCode, sum(Population) as res
    from city
    group by CountryCode
    having res > 3000000) as tabl;



-- Поменять запрос выше так, чтобы в результате вместо кода страны выводилось
-- ее название. Подсказка: нужен join таблиц city и country по полю CountryCode
select co.Name, sum(ci.Population) as res
from city as ci
inner join country as co
on ci.CountryCode = co.Code
group by CountryCode
having res > 3000000;


-- Вывести количество городов в каждой стране (CountryCode, amount of cities).
-- Подсказка: запрос по таблице city и группировка по CountryCode.
-- Поменять запрос так, чтобы вместо кодов стран, было названия стран.

select co.Name, count(ci.Name) as amount_of_cities
from city as ci
inner join country as co
on ci.CountryCode = co.Code
group by CountryCode;


-- Поменять запрос так, чтобы выводилось среднее количество городов в стране.

# Среднее количество городов в стране? Это что? Это как?
# Среднее - это сумма числовых значений деленных на их количество.
# Средняя зп, пенсий, средний бал.
# У каждой страны есть количество городов. Допустим у нас есть знаменатель.
# Числитель что??








