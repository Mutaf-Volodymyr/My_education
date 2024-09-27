use airport;

select * from clients;
select * from tickets;
select * from trips;
select * from airliners;


# Найдите всех клиентов, которые приобрели хотя бы один билет.
select *
from clients c
where exists(
    select *
    from tickets t
    where t.client_id = c.id);

SELECT DISTINCT c.name as client
FROM airport.clients c
WHERE c.id IN (
    SELECT t.client_id
    FROM airport.tickets t);

select
	distinct c.name as client
from clients as c
inner join
tickets as t
on c.id = t.client_id;

# Найдите все авиалайнеры, которые использовались хотя бы в одном рейсе.
select distinct model_name
 from airliners as air
 join trips as t
 on t.airliner_id = air.id;

# Найдите все рейсы, выполняемые авиалайнерами, произведёнными после 2010 года.
select *
from trips t
where exists(
    select 1
    from airliners a
    where t.airliner_id = a.id and a.production_year > 2010);

# Найдите максимальную цену билета в классе обслуживания 'Economy'.
select max(price)
from tickets
where service_class = 'Economy';

select *
from tickets
where service_class = 'Economy'
order by price desc
limit 1;

select *
from tickets t1
where service_class = 'Economy' and not exists(
    select 1
    from tickets t2
    where service_class = 'Economy'and t2.price > t1.price);

# Найдите всех клиентов, которые приобрели более одного билета.

SELECT *
FROM airport.clients c
INNER JOIN (
    SELECT client_id
    FROM airport.tickets
    GROUP BY client_id
    HAVING COUNT(id) > 1
) t ON t.client_id = c.id;
