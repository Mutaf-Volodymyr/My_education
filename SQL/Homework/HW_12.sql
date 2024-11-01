-- 1. Вывести количество городов для каждой страны. Результат должен содержать CountryCode,
-- CityCount (количество городов в стране). Поменяйте запрос с использованием джойнов так,
-- чтобы выводилось название страны вместо CountryCode.
use world;
select c.Name, count(ci.ID) as CityCount
from city as ci
inner join world.country c
on ci.CountryCode = c.Code
group by c.Name;


-- 2. Используя оконные функции, вывести список стран с
-- продолжительностью жизнью и средней продолжительностью жизни.

select Name,
       LifeExpectancy,
       avg(LifeExpectancy) over() as avg_LE
from country;


-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.

select Name,
       LifeExpectancy,
       dense_rank() over (order by LifeExpectancy desc ) as rang_LE
from country;



-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни.
with tab as (
    select Name,
           LifeExpectancy,
           dense_rank() over (order by LifeExpectancy desc ) as rang_LE
    from country)
select *
from tab
where rang_LE = 3;
