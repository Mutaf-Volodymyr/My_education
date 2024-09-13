-- JOIN ALL

-- INNER JOIN -- выборка по пересечению
-- CROSS JOIN -- Декартово произведение
-- LEFT JOIN -- выборка по пересечению + NULL правой таблички
-- RIGHT JOIN -- выборка по пересечению + NULL левой таблички
-- FULL JOIN -- выборка по всем пересечениям + NULL по всем
-- NATURAL JOIN -- выборка по вязями первичного и вторичного ключа
-- SELF JOIN -- выборка с этой же таблички

SELECT
e.first_name,
e.email,
e.job_id,
e.hire_date,
d.department_name
FROM employees as e
LEFT JOIN departments as d
ON e.department_id = d.department_id
AND d.location_id = 2500;


select
e.first_name as emp_name,
e1.first_name as mang_name
from employees as e
left join employees as e1
on e.manager_id = e1.employee_id;

use hr;
# Вывести имя, фамилию и должность сотрудника, название департамента и страны, где он расположен.
# Нужны только данные по региону Europe.

select * from employees;
select * from departments;
select * from locations;
select * from countries;
select * from regions;

select emp.first_name, emp.last_name, j.job_title, dep.department_name, t.country_name
from employees as emp
inner join jobs as j
    on emp.job_id = j.job_title
inner join departments as dep
    on emp.department_id = dep.department_id
inner join locations as loc
    on dep.location_id= loc.location_id
inner join (
        select country_id, country_name
        from countries
        where region_id = (
            select region_id
            from regions
            where region_name = 'Europe')
    ) as t on loc.country_id = t.country_id;





