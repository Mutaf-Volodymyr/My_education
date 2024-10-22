# Для каждого сотрудника вычислите среднюю зарплату в его отделе
# и в компании, а затем определите, где его зарплата выше — по сравнению
# со средней по отделу или по компании.

use hr;
select *, (case
    when t.salary > t.avg_company and t.salary > t.avg_department then "both_above"
    when t.salary = t.avg_company then "= avg_company"
    when t.salary = t.avg_department then "= department"
    when t.salary between avg_company and t.avg_department then "between comp and depatrt"
    else "below of both"
    end ) as rang_salary
from (
    select employee_id, concat(first_name, " ", last_name) as full_name, department_id, salary, job_id,
    avg(salary) over() as avg_company,
    avg(salary) over(partition by department_id) as avg_department
    from hr.employees
     ) as t
order by department_id desc;


# Для каждого пациента вычислите общее количество дней, проведённых на
# лечении. Затем определите среднее количество дней на пациента.
use medical_healthcare;



