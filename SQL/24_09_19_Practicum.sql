use hr;

# Найти сотрудников чья зарплата выше средней зарплаты по их департаменту
select emp.first_name,
       emp.last_name,
       emp.salary,
       salary_ave,
       dep. department_name
from employees as emp
inner join (
    select department_id, round(avg(salary), 2) as salary_ave
    from employees
    group by department_id) as avg_sal
on emp.department_id = avg_sal.department_id
inner join departments as dep
    on emp.department_id = dep.department_id
where emp.salary > avg_sal.salary_ave
order by emp.salary desc;


# получить список сотрудников с оценкой зарплаты:
# < 5000 - 'Low Salary', 5000 - 15000 - 'Medium Salary', > 15000 - 'High Salary'

select first_name, last_name, salary,  (case
        when salary < 5000 then 'Low Salary'
        when salary > 15000 then 'High Salary'
        when salary between 5000 and 15000 then 'Medium Salary' end) as category
from employees;

# Найти статьи, которые были написаны пользователями с ролью "moderator" или "author".
# Имя и фамилия автора должны быть представлены в одной колонке разом.

use social_media;

select * from user;
select * from news;
select * from role;
select * from comment;

select concat(u.last_name, ' ', u.first_name) as name, n.title, r.name as role
from news as n
inner join user as u
    on n.author_id = u.id
inner join role as r
    on u.role_id = r.id
where r.name in ("moderator", "author");

# Найти пользователей, у которых был создан хотя бы один комментарий к статье с заголовком,
# начинающимся на "A" или "B".

select com.content, concat(u.last_name, ' ', u.first_name) as name, n.title
from comment as com
inner join news as n
    on com.news_id = n.id
inner join user as u
    on com.author_id = u.id
where n.title like 'A%' or n.title like 'B%';

# Найти страны, где официальный язык — английский, и посчитать общее население городов в этих странах.


use world;
select * from country;
select * from countrylanguage;
select * from city;


select c.Name, cl.Language, c.Population
from country c
inner join countrylanguage cl
on c.Code = cl.CountryCode
    and cl.Language = 'English'
    and cl.IsOfficial = 'T';

# Найти страны, где официальный язык — английский, и посчитать общее население городов в этих странах.









