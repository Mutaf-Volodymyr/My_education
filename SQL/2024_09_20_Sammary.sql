-- Выведите одним запросом общее количество департаментов (отделов) в базе, кол департаментов
-- где есть сотрудники и кол департаментов где нет сотрудников (на выходе три столбца и одна строчка)
use hr;

select distinct count(dep.department_id) as all_dep,
        count(case
    when emp.employee_id is not null then dep.department_id end) dep_with_emp,
    count(case
    when emp.employee_id is null then dep.department_id end) dep_without_emp
    from departments as dep
left join employees as emp
    on dep.department_id = emp.department_id;


