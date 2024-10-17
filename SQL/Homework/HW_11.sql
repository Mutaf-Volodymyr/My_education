-- Подключиться к базе данных hr
use hr;

-- Вывести список region_id, total_countries, где total_countries - количество стран в таблице.
# Подсказка: работаем с таблицей countries, использовать оконную функцию over() и суммировать count(country_id).
select region_id,
       count(country_id) over() as total_countries
from countries;



-- Изменить запрос 2 таким образом, чтобы для каждого region_id выводилось количество стран в этом регионе.
# Подсказка: добавить partition by region_id в over().
select distinct region_id,
       count(country_id) over(partition by region_id) as total_countries
from countries;

-- Работа с таблицей departments. Написать запрос, который выводит location_id, department_name, dept_total, где dept_total - количество департаментов в location_id.

select location_id, department_name,
       count(department_name) over (partition by location_id) as dept_total
from departments;

-- Изменить запрос 3 таким образом, чтобы выводились названия городов соответствующих location_id.
select l.city, department_name,
       count(department_name) over (partition by d.location_id) as dept_total
from departments as d
inner join locations as l
on d.location_id=l.location_id;


-- Работа с таблицей employees. Вывести manager_id, last_name, total_manager_salary, где total_manager_salary - общая зарплата подчиненных каждого менеджера (manager_id).
select manager_id, last_name,
       sum(salary) over(partition by manager_id) as total_manager_salary
from employees;