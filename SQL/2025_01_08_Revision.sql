use sakila;

# Используя базу sakila, выведите фильмы, в названии которых содержится слово “LION”,
# посчитайте количество таких фильмов.
select *
from film
where title like "%LION%";

select count(*)
from film
where title like "%LION%";

select film_id, title,
       count(*) over() as count_all
from film
where title like "%LION%";

# Выведите названия всех фильмов в категории “Horror”.
select f.film_id, f.title
from film as f
inner join film_category as fc
on f.film_id = fc.film_id
inner join category as c
on fc.category_id = c.category_id
and c.name = 'Horror'

