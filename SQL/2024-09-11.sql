# JOIN
# Сервер на запись
select * from user;
select * from role;

# cross join - перемножает все на все (Декартово произведение)
select user.id,
       user.first_name,
       user.last_name,
       user.email,
       role.name as role_name
from user
cross join role;

# inner join - создает привязку одного значения одной таблицы
#               со значением в другой таблице (полное совпадение)
select
    u.id,
    u.first_name,
    u.email,
    u.role_id,
    r.name as role_name
from user as u
inner join role as r
on u.role_id = r.id;

select
    user.id,
    user.first_name,
    user.last_name,
    user.email,
    user.rating,
    user.role_id,
    news.title as news_title,
    news.moderated as news_moderated
from user
inner join news
on user.id = news.author_id
order by id;

# сервер на чтение
use hr;

select
    employees.first_name,
    employees.last_name,
    departments.department_name
from employees
inner join departments
    on employees.department_id = departments.department_id
order by department_name, first_name;

# left join (left outer join)
# Сервер на запись

use l_7_practice_290724;
select
    u.id,
    u.email,
    u.rating,
    n.id as news_id,
    n.title,
    n.moderated
from l_7_practice_290724.user as u
left join l_7_practice_290724.news as n
on u.id = n.author_id;


# right join (right outer join)
# Сервер на запись
select
    u.id,
    u.email,
    u.rating,
    n.id as news_id,
    n.title,
    n.moderated
from l_7_practice_290724.user as u
right join l_7_practice_290724.news as n
on u.id = n.author_id;

# ЗАДАЧИ
# сервер на чтение

# Выведите названия департаментов, где есть сотрудники с зп больше 15000.
use hr;
select department_name
from departments
inner join hr.employees as e
    on departments.department_id = e.department_id
where e.salary > 15000
group by department_name;

# фильтрация перед присоединением
select department_name
from departments
inner join hr.employees as e
    on departments.department_id = e.department_id
    and e.salary > 15000
group by department_name;

# Напишите запрос, который покажет имя и фамилию сотрудников,
# которые получают зп больше своего менеджера
use hr;
select
    e.first_name,
    e.last_name,
    e.salary as sal_emp,
    e2.salary as sal_man,
    e2.first_name as name_maneger,
    e2.last_name as sername_meneger
from employees as e
inner join hr.employees as e2
    on e.manager_id = e2.employee_id
    and e.salary > e2.salary;

# Сервер на запись
use l_7_practice_290724;
select * from CUSTOMERS;
select * from ORDERS;
select * from SELLERS;



# Выведите имена всех продавцов. Предусмотрите также в выборке имена
# их боссов, сформировав атрибут boss_name. В выборке должно присутствовать
# два атрибута — sname, boss_name.
select
    t1.SNAME as seller,
    t2.SNAME as boss
from SELLERS as t1
left join SELLERS as t2
    on t1.BOSS_ID = t2.ID;


# Для каждого сотрудника выведите разницу между комиссионными его босса и его
# собственными. Если у сотрудника босса нет, выведите NULL.
# Вывести : sname, difference.

select
    t1.SNAME as sname,
    t2.COMMISSION - t1.COMMISSION as difference
#     t2.COMMISSION as bos_com,
#     t1.COMMISSION as sal_com
from SELLERS as t1
left join SELLERS as t2
    on t1.BOSS_ID = t2.ID;

# Выведите пары покупателей и обслуживших их продавцов из одного города.
# Вывести: sname, cname, city

select
    s.SNAME,
    c.CNAME,
    s.CITY as CITY_S
from ORDERS as o
inner join CUSTOMERS as c
on o.CUST_ID = c.ID
inner join SELLERS as s
on o.SELL_ID = s.ID
WHERE s.CITY = c.CITY;





