use hr;

# выведите номера отделов и количество сотрудников в каждом отделе,
# где сотрудников больше 10
select d.department_name, count(*) as count_emp
from employees as e
inner join departments as d
on e.department_id = d.department_id
group by d.department_id
having count_emp > 10;

# Найти максимальную зарплату в каждом департаменте.
# Вывести department_id и max_salary

select d.department_id, d.department_name, max(e.salary) as mx_sal
from employees as e
inner join departments as d
on e.department_id = d.department_id
group by d.department_id;

# Найти сотрудников, у которых наибольшая зарплата в их департаменте
select e.employee_id, e.first_name, e.last_name, max(e.salary), e.department_id, d.department_name
from employees as e
inner join departments as d
on d.department_id = e.department_id
group by e.department_id;

select e.employee_id, e.first_name, e.last_name, e.salary, sal_max.mx_sal, sal_max.mx_sal
from employees as e
inner join (
    select em.department_id, max(em.salary) as mx_sal
    from employees as em
    group by em.department_id) as sal_max
    on sal_max.mx_sal = e.salary ;


select *
from employees
where department_id = 50;

SELECT
    t1.first_name,
    t1.last_name,
    t1.department_id,
    t1.salary
FROM employees t1
INNER JOIN (
    SELECT
    department_id,
    MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id ) t2
    ON t1.department_id = t2.department_id
    AND t1.salary = t2.max_salary;


# Выведите название стран и количество лет, прошедших с момента их независимости до текущего года.
# Отобразите только те страны, которые получили независимость более 50 лет назад. Результат должен быть
# отсортирован по количеству лет независимости в порядке убывания.


use world;

select Name, (year(now()) - abs(IndepYear)) as year_indep
from country
where
    IndepYear is not null
    and year(now()) - abs(IndepYear) > 50
order by year_indep desc;


# Найдите все страны, у которых официальным языком является французский (French), и у которых
# население превышает 5 миллионов человек. Выведите название страны, ее население и континент.

select c.Name, c.Population, c.Continent
from country as c
inner join countrylanguage as cl
on c.Code = cl.CountryCode
and cl.Language = 'French' and cl.IsOfficial = 'T'
where Population > 5000000;

# Для каждого города вычислите, сколько лет прошло с момента основания страны, в которой
# он находится (используйте поле IndepYear), до текущего года. Выведите название города,
# название страны и количество лет. Отобразите только те города, где количество
# лет превышает 100.

select ci.Name, year(now()) - abs(c.IndepYear) as dif
from city as ci
inner join country as c
on c.Code = ci.CountryCode
    and c.IndepYear is not null
    and  year(now()) - abs(c.IndepYear) > 100;



# Для каждого континента определите средний ВНП (GNP) и количество стран,
# у которых ВНП выше среднего по континенту. Выведите название континента,
# средний ВНП и количество таких стран


select c.Continent, count(*) as result, continent_gnp.avg_gnp
from country as c
inner join (
    select Continent, avg((GNP)) as avg_gnp
    from country
    group by Continent) as continent_gnp
    on continent_gnp.Continent = c.Continent
    and c.GNP > continent_gnp.avg_gnp
group by c.Continent;



# Выведите новости, которые были модерированы, созданы в течение
# последних 6 месяцев (от 2022 года) и имеют менее 3
# комментариев. Отобразите название новости,
# дату создания и количество комментариев.
use social_media;

select n.title, count(*) as col_kom, n.created_at
from comment as c
inner join news as n
on n.id = c.news_id
    and moderated = 1
    and n.created_at > '2022-01-01' - interval 6 month
group by n.id
having col_kom >= 3;


# Выведите список новостей, которые были созданы авторами,
# зарегистрированными более 2 лет назад,
# и у которых нет комментариев. Выведите название новости,
# имя и фамилию автора, дату создания новости.

select n.title, u.first_name, u.last_name, n.created_at
from news as n
inner join user as u
on u.id = n.author_id
    and n.created_at > now()-interval 2 year
left join comment as c
on n.id = c.news_id
where c.content is null;

SELECT u.id as user_id, n.id, u.first_name, u.last_name, n.title, n.created_at, c.content
FROM social_media.news n
inner join user u
	on u.id = n.author_id
    and year(now()) - year(u.created_at) > 2
left join comment c
	on c.news_id = n.id
where c.content is NULL;





