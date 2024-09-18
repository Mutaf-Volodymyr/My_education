
############# агрегирующее функции и группировки #################

use hr;

select e.first_name, e.last_name, e.salary, d.department_name
from employees as e
inner join departments as d
    on e.department_id = d.department_id
where e.salary between (select avg(salary)
    from employees) and (select max(salary)
    from employees)
order by e.salary desc;


# Найти имена и фамилии сотрудников с максимальной зарплатой HR.EMPLOYEES:
select e.first_name, e.last_name, e.salary, d.department_name
from employees as e
inner join departments as d
    on e.department_id = d.department_id
where e.salary = (select max(salary)
    from employees);

# Получить список департаментов и сотрудников, которые работают
# в департаментах с количеством сотрудников больше 5

select e.first_name,
       e.last_name,
       dep.department_name as d_name,
       e.department_id as d_id
from employees as e
inner join (
    select count(e.department_id) as co, department_id
    from employees as e
    group by e.department_id
    having co > 5) as d
        on e.department_id = d.department_id
inner join departments as dep
on e.department_id = dep.department_id;


-- решение Кирила
SELECT d.department_name,
       e.first_name,
       e.last_name
FROM hr.employees e
INNER JOIN hr.departments d
    ON d.department_id = e.department_id
WHERE d.department_id IN (
    SELECT department_id
    FROM hr.employees e2
    GROUP BY e2.department_id
    HAVING COUNT(department_id) > 5);



# Получить Список сотрудников, чьи зарплаты выше
# средней зарплаты по департаментам, которые находятся
# в определённых странах

select * from employees;
select * from departments;
select * from locations;
select * from countries;

select emp.first_name,
       emp.last_name,
       emp.salary,
       salary_ave,
       dep. department_name,
       loc.city,
       loc.country_id
from employees as emp
inner join (
    select department_id, round(avg(salary), 2) as salary_ave
    from employees
    group by department_id) as avg_sal
on emp.department_id = avg_sal.department_id
inner join departments as dep
    on emp.department_id = dep.department_id
inner join locations as loc
    on dep.location_id = loc.location_id
    and country_id = 'US'
where emp.salary > avg_sal.salary_ave
order by emp.salary desc;















