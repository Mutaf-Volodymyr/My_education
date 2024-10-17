use shop;
# Средний рейтинг клиентов по городам: Для каждого города вывести средний рейтинг клиентов.

select distinct CITY,
       avg(RATING) over(partition by CITY) as abc
from CUSTOMERS;

# Вывести информацию о каждом заказе и максимальную сумму заказа
# в том же месяце для каждой строки.

select ORDER_ID,
       monthname(ODATE) as month_name,
       ORDERS.AMT,
       max(AMT) over (partition by month(ORDERS.ODATE)) as max_amt_of_month
from ORDERS;

# Для более полного понимания практической значимости прошлого запроса,
# добавим подсчет относительного вклада каждого заказа
# в общий объем продаж месяца.
select ORDER_ID,
       monthname(ODATE) as month_name,
       ORDERS.AMT,
       max(AMT) over (partition by month(ORDERS.ODATE)) as best_deal,
       sum(AMT) over (partition by month(ORDERS.ODATE)) as all_sel,
       concat(round(AMT / (sum(AMT) over (partition by month(ORDERS.ODATE))) * 100, 2), '%') as persent
from ORDERS;


# Вывести список продавцов с указанием общей суммы их продаж.
# Отсортировать продавцов по убыванию суммы продаж.

select *,
       coalesce(sum(O.AMT) over(partition by O.SELL_ID), 0) as sum_atm_by_seller
from SELLERS as s
left join shop.ORDERS O
    on s.SELL_ID = O.SELL_ID
order by sum_atm_by_seller desc;

# Вывести топ-2 продавцов с самой высокой средней суммой заказа.
select distinct s.SELL_ID, s.SNAME,
       round(avg(o.AMT) over(partition by o.SELL_ID), 2) as avg_amt
from SELLERS as s
left join shop.ORDERS o
    on s.SELL_ID = o.SELL_ID
order by avg_amt desc
limit 2;

################################################################
SELECT
    *,
    ROW_NUMBER() OVER (ORDER BY CUST_ID DESC) AS ROW_NUMBER_ID,
    RANK() OVER (ORDER BY CUST_ID DESC) AS RANK_ID,
    DENSE_RANK() OVER (ORDER BY CUST_ID DESC) AS DENSE_RANK_ID
    # NTILE(3) OVER (ORDER BY CUST_ID DESC) AS NTILE_ID
FROM ORDERS;

SELECT
    ORDER_ID,
    ODATE,
    AMT,
    SUM(AMT) OVER (ORDER BY ODATE) AS running_total,
    SUM(AMT) OVER (ORDER BY ODATE DESC) AS running_total_desc
FROM ORDERS;

#########################################################
use hr;
# Произведите ранжирование департаментов по средней зарплате



select *
#        d.department_name,
#        round(coalesce(e.avg_salary over(partition by d.department_name), 0), 2) as avg_sall,
#        dense_rank() over(order by coalesce(avg(avg_salary), 0) desc) as rang
from departments as d
left join (
    select department_id, round(avg(salary), 2) as avg_salary
    from employees
    group by department_id) as e
    on e.department_id=d.department_id
group by department_name;










# что тут происходит??
select employee_id, department_id, salary,
       avg(salary) over(order by department_id) as ord_by_dep_asc,
       avg(salary) over(order by department_id desc) as ord_by_dep_desc,
       avg(salary) over(partition by department_id) as part_by_dep
#        avg(salary) over(partition by department_id order by department_id) as part_and_ord_by_dep,
#        avg(salary) over(partition by department_id order by salary) as part_and_ord_by_dep_sal,
#        avg(salary) over(partition by department_id order by employee_id) as part_and_ord_by_dep_empid
from hr.employees;

# вывести информацию о сотрудниках (id департамента, зарплата, дата найма, средняя зарплата).
# расчёт средней зарплаты произвести по департаменту относительно даты найма в порядке возрастания.


select department_id, salary, hire_date,
       avg(salary) over(partition by department_id order by hire_date) as avg_dep_sall
from employees;

# Для каждого отдела department_id выведите сотрудников, добавив ранг зарплаты
# упорядочив по зарплате salary в порядке убывания.
select department_id, first_name, last_name, salary,
       dense_rank() over(partition by department_id order by salary desc)
from employees;


# Разбейте сотрудников на четыре равные группы по зарплате salary и выведите номер группы
# для каждого сотрудника
select department_id, first_name, last_name, salary,
       NTILE(4) over(order by salary desc) as gr
from employees;

select gr, avg(salary)
from (select department_id, first_name, last_name, salary,
       NTILE(4) over(order by salary desc) as gr
from employees) as t
group by gr;



# Найдите максимальную зарплату salary для каждой должности по отделам
select employee_id, department_id, job_id,
       max(salary) over(partition by department_id order by job_id) as mx_sal_dep_job
from employees;


# Выведите сотрудников, добавив номер строки для каждого менеджера manager_id,
# и отфильтруйте только первых трех по дате найма подчиненных каждого менеджера.
select employee_id, first_name, last_name, hire_date
from employees
where employee_id in (
    select manager_id
    from employees
    );

# Для каждого отдела department_id вычислите среднюю зарплату
# и выведите сотрудников, чья зарплата выше средней по отделу.
select e.employee_id, e.first_name, e.last_name, e.salary, t.avg_dep
from employees as e
inner join
    (select employee_id, avg(salary) over(partition by department_id) as avg_dep
    from employees) as t
    on e.employee_id=t.employee_id
where e.salary > t.avg_dep;

# вычислите среднюю зарплату по должности dep и отобразите
# процентное соотношение зарплаты каждого сотрудника к .
select e.employee_id, e.first_name, e.last_name, e.salary, e.job_id,
       sum(salary) over (partition by department_id) as avg_dep,
       salary / (sum(salary) over (partition by department_id)) * 100 as p
from employees as e;


# Разбейте сотрудников на группы по отделам и внутри каждого отдела распределите
# их на три равные части по зарплате.
select employee_id, first_name, last_name, department_id, salary,
       NTILE(3) over (partition by department_id order by salary)
from employees;


# определите, на каком месте по максимальной зарплате находится каждый отдел в компании.


select d.department_name, t.mx_sall,
        dense_rank() over (order by mx_sall desc) as pleace
from
    (select department_id,
           max(salary) as mx_sall
    from employees
    group by department_id) as t
inner join departments as d
on d.department_id=t.department_id;










