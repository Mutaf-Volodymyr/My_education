use hr;
select * from employees;

use social_media;
select * from user;

use world;

-- Найдите страну с наибольшей средней численностью населения среди всех ее городов. Укажите название страны и среднюю численность населения ее городов.
SELECT c2.Name, AVG(c.Population)
FROM world.city c
INNER JOIN world.country c2 ON c2.Code = c.CountryCode
GROUP BY c.CountryCode
ORDER BY AVG(c.Population) DESC
LIMIT 1;


-- Перечислите пять ведущих языков, на которых говорят в европейских странах (независимо
-- от официального статуса), а также общее количество стран Европы, где говорят на каждом
-- из них. Упорядочьте результаты по количеству стран в порядке убывания.


select cl.Language, count(distinct c.Code) as country_count
from countrylanguage cl
inner join world.country c
    on cl.CountryCode = c.Code
    and c.Continent = 'Europe'
group by cl.Language
order by country_count desc;


# Покажите все страны, в которых на всех официальных языках говорит более 50 %
# населения.Укажите код страны и названия этих стран.

select c.Name, sum(Percentage) as sum_pr
from country c
inner join world.countrylanguage cl
    on c.Code = cl.CountryCode
    and cl.IsOfficial = 'T'
group by c.Name
having  sum_pr > 50
order by sum_pr desc; -- 132

select *
from country c
where not EXISTS(
    select 1
    from countrylanguage cl
    where IsOfficial = 'T' and Percentage <= 50 and cl.CountryCode = c.Code);


use hr;
SELECT department_name
FROM departments d
WHERE EXISTS (
    SELECT *
    FROM employees e
    WHERE e.department_id = d.department_id);


# Перечислите названия стран, в которых есть город с таким же названием, как и сама страна.
use world;
select c.Name
from country c
where exists(
    select 1
    from city ci
    where ci.Name = c.Name);


# Найдите языки, которые являются официальными как минимум в двух разных странах.
# Укажите название языка и количество стран, в которых он является официальным.

select cl.Language, count(CountryCode) as cou
from countrylanguage as cl
where IsOfficial = 'T'
group by Language
having cou > 1;




-- Перечислите пять ведущих языков, на которых говорят в европейских странах (независимо
-- от официального статуса), а также общее количество стран Европы, где говорят на каждом
-- из них. Упорядочьте результаты по количеству стран в порядке убывания.

select cl.Language, sum((Population * Percentage / 100)) as kol
from countrylanguage cl
inner join country c
    on cl.CountryCode = c.Code
    and c.Continent = 'Europe'
group by Language
order by kol desc;


# Перечислите страны, в которых население столицы составляет менее 10 % от всего
# населения страны. Укажите название страны, название столицы и численность населения.

select co. Name
from country co
where exists(
    select 1
    from city ci
    where co.Capital = ci.ID and (ci.Population * 100 /  co.Population) < 10);

select c.Name as Country_name
from country as c
join city as ct
on c.Capital = ct.ID
where ct.Population < c.Population * 0.10;




